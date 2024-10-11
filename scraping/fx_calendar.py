from bs4 import BeautifulSoup
import pandas as pd
import requests
from dateutil import parser


def get_date(child_element):
    tr = child_element.select_one('tr')
    ths = tr.select('th')
    for th in ths:
        if th.has_attr("colspan"):
            date_text = th.get_text().strip()
            return parser.parse(date_text)
    return None

def get_table_data(item_date, table_rows):
    data =[]
    for tr in table_rows:
        data.append(dict(
            date=item_date,
            country=tr.attrs['data-country'],
            category=tr.attrs['data-category'],
            event= tr.attrs['data-event'],
            symbol = tr.attrs['data-symbol'],

        ))
    return data
def fx_calendar():

    session = requests.Session()


    headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Cookie": "calendar-importance=3;cal-custom-range=2022-03-23 00:00|2022-03-25 00:00; TEServer=TEIIS3; cal-timezone-offset=0;"
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
    [print(x) for x in final_data]
        