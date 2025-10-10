

import pandas as pd
import numpy as np
import glob
import os
from graph import create_plot

columns = [
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_volume', 'trades', 
        'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
    ]

def main():
    """
    Description:

    """    
    this_path = os.path.dirname(__file__)
    binance_data_path = glob.glob(os.path.join(this_path, "*.csv"))    

    for data in binance_data_path:
        
        dir_name = os.path.join(this_path, os.path.dirname(data))
        os.makedirs(dir_name, exist_ok=True)

        # loading data as a DataFrame
        df = pd.read_csv(data, names=columns)
        df = df.drop(columns=['close_time', 'quote_volume', 'trades', 'taker_buy_quote_volume','ignore'])

        df['open_time'] = df['open_time']/1_000_000
        df['open_time'] = df['open_time']-df['open_time'].min()

        df['delta'] = df['close'] - df['open']
        hm_dm2 = df[df['delta']>20]                 # 20 U$ candles

        df['mid_price'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
        df['mid_price_rolling_7'] = df['mid_price'].rolling(window=7).mean()
        df['mid_price_ewm_3'] = df['mid_price'].ewm(span=3, adjust=False).mean()

        df['volume_growth'] = df['volume'].pct_change() * 100

        idx = hm_dm2.index

        for i in idx:

            analyse_df = df.iloc[i-10:i+1]
            print(analyse_df)

            create_plot(df, i)

            print('HERE')








if __name__ == "__main__":
    main()




"""

# Média dos 3 preços principais: High, Low, Close
df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3
# Dá mais peso ao preço de fechamento
df['weighted_close'] = (df['high'] + df['low'] + (2 * df['close'])) / 4
# Média dos 4 preços do candlestick
df['ohlc_avg'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4

# Média móvel simples do preço de fechamento
df['sma_5'] = df['close'].rolling(window=5).mean()
df['sma_10'] = df['close'].rolling(window=10).mean()

# Média móvel exponencial (dá mais peso aos preços recentes)
df['ema_5'] = df['close'].ewm(span=5, adjust=False).mean()
df['ema_10'] = df['close'].ewm(span=10, adjust=False).mean()

# Derivada
df['ema_5_diff'] = df['ema_5'].diff()
df['ema_10_diff'] = df['ema_10'].diff()

# Média móvel do typical price
df['typical_price_sma'] = df['typical_price'].rolling(window=10).mean()
df['typical_price_ema'] = df['typical_price'].ewm(span=10, adjust=False).mean()

"""
