import pandas as pd

def create_excel(df_ma_res, df_ma_trades,granularity):
    filename = f"{granularity}"


if __name__ == "__main__":
    df_ma_res = pd.read_pickle("../data/ma_res.pkl")
    df_ma_trades = pd.read_pickle("../data/ma_trades.pkl")
    create_excel(df_ma_res, df_ma_trades, "H1")