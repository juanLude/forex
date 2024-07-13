import pandas as pd

def BollingerBands(df: pd.DataFrame, n, s):
    typical_price = (df.mid_c + df.mid_h + df.mid_l) / 3    
    stddev = typical_price.rolling(window=n).std()
    df['BB_MA'] =  typical_price.rolling(window=n).mean()
    df['BB_UP'] = df['BB_MA'] + s * stddev
    df['BB_LW'] = df['BB_MA'] - s * stddev

    return df
