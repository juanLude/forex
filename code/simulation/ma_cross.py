import pandas as pd
from infrastructure.instrument_collection import instrumentCollection as ic

BUY = 1
SELL = -1
NONE = 0
get_ma_col = lambda period: f'MA_{period}'

def is_trade(row):
    if row['DELTA'] > 0 and row['DELTA_PREV'] <= 0:
        return BUY
    elif row['DELTA'] < 0 and row['DELTA_PREV'] >= 0:
        return SELL
    else:
        return NONE
def load_price_data(pair, granularity, ma_list):
    df = pd.read_pickle(f'./exploration/data/{pair}_{granularity}.pkl')
    for ma in ma_list:
        df[get_ma_col(ma)] = df.mid_c.rolling(window=ma).mean()
    df.dropna(inplace=True)
    df.reset_index(drop=True,inplace=True)
    return df


def assess_pair(price_data, ma_long, ma_short, instrument):
    df_analysis = price_data.copy()
    df_analysis['DELTA'] = df_analysis[ma_short] - df_analysis[ma_long]
    df_analysis['DELTA_PREV'] = df_analysis['DELTA'].shift(1)
    df_analysis['TRADE'] = df_analysis.apply(is_trade, axis=1)
    print(instrument.name, ma_long, ma_short)
    print(df_analysis.tail(3))
    return None
def analyse_pair(instrument, granularity, ma_long,ma_short):
    ma_list = set(ma_long + ma_short)
    pair = instrument.name
    print(f"Analysing {pair} with granularity {granularity}")
    price_data = load_price_data(pair, granularity, ma_list)
    print(price_data.tail(3))

    for ma_l in ma_long:
        for ma_s in ma_short:
            if ma_s >= ma_l:
                continue
            result = assess_pair(price_data, get_ma_col(ma_l), get_ma_col(ma_s), instrument)



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
