import pandas as pd
from infrastructure.instrument_collection import instrumentCollection as ic

BUY = 1
SELL = -1
NONE = 0
get_ma_col = lambda period: f'MA_{period}'

def load_price_data(pair, granularity, ma_list):
    df = pd.read_pickle(f'./exploration/data/{pair}_{granularity}.pkl')
    for ma in ma_list:
        df[get_ma_col(ma)] = df.mid_c.rolling(window=ma).mean()
    df.dropna(inplace=True)
    df.reset_index(drop=True,inplace=True)
    return df
  
def analyse_pair(instrument, granularity, ma_long,ma_short):
    ma_list = set(ma_long + ma_short)
    pair = instrument.name
    print(f"Analysing {pair} with granularity {granularity}")
    price_data = load_price_data(pair, granularity, ma_list)
    print(price_data.tail(3))



def run_ma_simulation(curr_list=["EUR", "USD", "GBP", "JPY"],
                      granularity=["H1"],
                      ma_long=[20,40,80],
                        ma_short=[10,20]):

    ic.LoadInstruments("./exploration/data")
    for g in granularity:
        for p1 in curr_list:
            for p2 in curr_list:
                pair = f"{p1}_{p2}"
                if pair in ic.instruments_dict.keys():
                    analyse_pair(ic.instruments_dict[pair], g, ma_long, ma_short)
