

import pandas as pd
import numpy as np
import glob
import os
from graph import create_plot


def main():
    """
    Description:

    """

    
    this_path = os.path.dirname(__file__)
    binance_data_path = glob.glob(os.path.join(this_path, "*.csv"))    

    binance_data_ex = binance_data_path[0]

    columns = [
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_volume', 'trades', 
        'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
    ]
    
    # loading data as a DataFrame
    df = pd.read_csv(binance_data_ex, names=columns)
    df.drop(['quote_volume', 'trades'], axis=1)
    # Treating DataFrame data
    # df['open_time'] = df['open_time'] / 1_000_000
    # df['open_time'] = df['open_time'] - df['open_time'].min()
    # df['close_time'] = df['close_time'] / 1_000_000
    # df['close_time'] = df['close_time'] - df['close_time'].min() + 1

    # min_quote_volume, max_quote_volume = df['quote_volume'].min(), df['quote_volume'].max()
    min_volume, max_volume = df['volume'].min(), df['volume'].max()

    # print(f"Min Volume: {min_volume}")
    # print(f"Max Volume: {max_volume}")

    # Média dos 3 preços principais: High, Low, Close
    df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3
    # Dá mais peso ao preço de fechamento
    df['weighted_close'] = (df['high'] + df['low'] + (2 * df['close'])) / 4
    # Média dos 4 preços do candlestick
    df['ohlc_avg'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4

    # Média móvel simples do preço de fechamento
    df['sma_5'] = df['close'].rolling(window=5).mean()
    df['sma_10'] = df['close'].rolling(window=10).mean()
    df['sma_20'] = df['close'].rolling(window=20).mean()

    # Média móvel exponencial (dá mais peso aos preços recentes)
    df['ema_5'] = df['close'].ewm(span=5, adjust=False).mean()
    df['ema_10'] = df['close'].ewm(span=10, adjust=False).mean()
    df['ema_20'] = df['close'].ewm(span=20, adjust=False).mean()

    # Derivada
    df['ema_5_diff'] = df['ema_5'].diff()
    df['ema_10_diff'] = df['ema_10'].diff()
    df['ema_20_diff'] = df['ema_20'].diff()

    # Média móvel do typical price
    df['typical_price_sma'] = df['typical_price'].rolling(window=10).mean()
    df['typical_price_ema'] = df['typical_price'].ewm(span=10, adjust=False).mean()

    
    print(df[df['volume']>np.mean([min_volume, max_volume])])
    # print(df[df['quote_volume']>np.mean([min_quote_volume, max_quote_volume])])
    create_plot(df, 51011, 40)


    print('HERE')







if __name__ == "__main__":
    main()

