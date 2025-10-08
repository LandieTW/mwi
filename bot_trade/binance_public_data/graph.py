

import pandas as pd
import mplfinance as mpf


def create_plot(data: pd.DataFrame, ini: int, n_time: int):

    data = data.iloc[ini:ini+n_time]  # 1 hour

    data['open_time'] = pd.to_datetime(data['open_time'], unit='us')
    data = data.set_index('open_time')

    # Selecionar apenas as colunas necessárias na ordem correta
    df_candle = data[['open', 'high', 'low', 'close', 'volume', 'ema_5_diff', 'ema_10_diff', 'ema_20_diff']]

    apds = [
        mpf.make_addplot(df_candle['ema_5_diff'], color='blue', width=2.0, linestyle='-', label='SMA 5'),
        mpf.make_addplot(df_candle['ema_10_diff'], color='red', width=2.0, linestyle='--', label='SMA 10'),
        mpf.make_addplot(df_candle['ema_20_diff'], color='orange', width=2.0, linestyle=':', label='SMA 20'),
        # mpf.make_addplot(df_candle['ema_10'], color='purple', width=1.5, linestyle='-.', label='EMA 10')
    ]

    mpf.plot(df_candle, 
         type='candle',
         style='charles',
         title='Candlestick - BTC/USDT com Médias',
         ylabel='Preço (USDT)',
         volume=True,
         addplot=apds,
         figratio=(12, 8))
