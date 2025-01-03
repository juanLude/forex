from bs4 import BeautifulSoup
import pandas as pd
import requests
from dateutil import parser
import time
import datetime as dt
import random

from db.db import DataDB

pd.set_option('display.max_rows', None)

def get_date(child_element):
    tr = child_element.select_one('tr')
    ths = tr.select('th')
    for th in ths:
        if th.has_attr("colspan"):
            date_text = th.get_text().strip()
            return parser.parse(date_text)
    return None

def get_data_point(key, element):
    for e in['span', 'a']:
        d = element.select_one(f"{e}#{key}")
        if d is not None:
            return d.get_text()
    return ''

def get_data_for_key(tr,key):
    if tr.has_attr(key):
        return tr.attrs[key]
    return ''
def get_table_data(item_date, table_rows):
    data =[]
    for tr in table_rows:
        data.append(dict(
            date=item_date,
            country=get_data_for_key(tr,'data-country'),
            category=get_data_for_key(tr,'data-category'),
            event=get_data_for_key(tr,'data-event'),
            symbol=get_data_for_key(tr,'data-symbol'),
            actual = get_data_point('actual', tr),
            previous = get_data_point('previous', tr),
            forecast = get_data_point('forecast', tr)
        ))
    return data
def get_fx_calendar(from_date):

    session = requests.Session()

    from_date_str = dt.datetime.strftime(from_date, '%Y-%m-%d 00:00:00')
    to_date = from_date + dt.timedelta(days=6)
    to_date_str = dt.datetime.strftime(to_date, '%Y-%m-%d 00:00:00')

    headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Cookie": f"calendar-importance=3;cal-custom-range={from_date_str}|{to_date_str}; TEServer=TEIIS3; cal-timezone-offset=0;"
    }
    resp = session.get('https://tradingeconomics.com/calendar', headers=headers)

    soup = BeautifulSoup(resp.content, 'html.parser')

    table = soup.select_one("table#calendar")
    
    last_header_date = None

    trs = {}
    final_data = []

    for c in table.children:
        if c.name == 'thead':
            if 'class' in c.attrs and 'hidden-head' in c.attrs['class']:
                continue
            last_header_date= get_date(c)
            trs[last_header_date] =[]
        elif c.name == 'tr':
            trs[last_header_date].append(c)
    
    for item_date, tabale_rows in trs.items():
        final_data += get_table_data(item_date, tabale_rows)
    #[print(x) for x in final_data]
    return final_data

def fx_calendar():
    #final_data = []

    start = parser.parse("2021-05-03T00:00:00Z")
    end = parser.parse("2022-03-25T00:00:00Z")

    database = DataDB()

    while start < end:
        
        data = get_fx_calendar(start)
        print(start,len(data))
        database.add_many(DataDB.CALENDAR_COLLECTION, data)
        start = start + dt.timedelta(days=7)
        time.sleep(random.randint(1,3))
    
    #print(pd.DataFrame.from_dict(final_data))