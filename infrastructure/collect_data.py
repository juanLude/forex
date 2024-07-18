import pandas as pd
import datetime as dt
from dateutil import parser

from infrastructure.instrument_collection import InstrumentCollection
from api.oanda_api import OandaApi

CANDLE_COUNT = 3000

INCREMENTS = {
    'M5': 5 * CANDLE_COUNT,
    'H1': 60 * CANDLE_COUNT,
    'H4': 240 * CANDLE_COUNT,
}

def save_file(final_df: pd.DataFrame, file_prefix, granularity,pair):
    filename = f"{file_prefix}{pair}_{granularity}.pkl"

    final_df.drop_duplicates(subset=["time"], inplace=True)
    final_df.sort_values(by=["time"],inplace=True)
    final_df.reset_index(drop=True, inplace=True)
    final_df.to_pickle(filename)
    
    s1 = f"*** {pair} {granularity} {final_df.time.min()} {final_df.time.max()}"
    print(f"*** {s1} --> {final_df.shape[0]} candles ***")


def fetch_candles(pair, granularity, date_from: dt.datetime, date_to: dt.datetime, api: OandaApi):
    
    attemps = 0
    while attemps < 3:
        try:
            return api.fetch_candles(pair,granularity=granularity,date_from=date_from,date_to=date_to)
        except Exception as e:
            print(e)
            attemps += 1
    
    
    return None

def collect_data(pair, granularity,date_from: dt.datetime, date_to: dt.datetime, file_prefix,   api: OandaApi):
    
    time_step = INCREMENTS[granularity]

    end_date = parser.parse(date_to)
    from_date = parser.parse(date_from)

    candle_dfs = []

    to_date = from_date

    while to_date < end_date:
        from_date = to_date
        to_date = from_date + dt.timedelta(minutes=time_step)
        if to_date > end_date:
            to_date = end_date

        candles = fetch_candles(pair, granularity, from_date, to_date, api)
        candles = pd.DataFrame(candles)

        if candles is not None:
            candle_dfs.append(candles)
            print(f"{pair} {granularity} {from_date} {to_date} --> {candles.shape[0]} candles loaded")
        else:
            print(f"{pair} {granularity} {from_date} {to_date} --> NO CANDLES")
        
        from_date = to_date

    if len(candle_dfs) > 0:
        final_df = pd.concat(candle_dfs)
        save_file(final_df, file_prefix, granularity,pair)
    else:
        print(f"{pair} {granularity} --> NO DATA SAVED")
def run_collection(ic: InstrumentCollection, api: OandaApi ):
    our_curr = ["EUR", "USD","CAD","AUD","GBP","NZD", "JPY"]

    for p1 in our_curr:
        for p2 in our_curr:
            pair = f"{p1}_{p2}"
            if pair in ic.instruments_dict.keys():
                for granularity in ["M5","H1","H4"]:
                    print(pair, granularity)
                    collect_data(
                        pair, 
                        granularity,
                        "2016-01-07T00:00:00Z",
                        "2021-12-31T00:00:00Z",
                        "./data/",
                        api
                    )
