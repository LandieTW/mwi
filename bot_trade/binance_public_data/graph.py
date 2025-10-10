

import pandas as pd
import matplotlib.pyplot as plt

def create_plot(data: pd.DataFrame, line: int):

    start = max(line-30, 0)
    end = line+30 if start > 0 else 60

    df_plot = data.iloc[start:end]
    
    # Criar subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), 
                                   gridspec_kw={'height_ratios': [3, 1]})
    
    # SUBPLOT 1 - PREÇO
    ax1.plot(df_plot['open_time'], df_plot['mid_price'], color='blue', linewidth=2, label='Mid_price')
    ax1.plot(df_plot['open_time'], df_plot['mid_price_rolling_7'], color='black', linewidth=2, label='Rolling Mean 7')
    ax1.plot(df_plot['open_time'], df_plot['mid_price_ewm_3'], color='red', linewidth=2, label='EWM Mean 3')
    # ax1.plot(df_plot['open_time'], df_plot['ohlc_avg'], color='green', linewidth=2, label='Mid_price')
    
    ax1.set_title(f'BTC/USDT - Preço e Volume', 
                  fontsize=14, fontweight='bold')
    ax1.set_ylabel('Preço (USDT)', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # SUBPLOT 2 - VOLUME
    ax2.plot(df_plot['open_time'], df_plot['volume'], color='orange', linewidth=1, label='Volume')
    ax2.bar(df_plot['open_time'], df_plot['volume_growth'], color='green', alpha=.5, label='Growth')
    
    ax2.set_xlabel('Data/Hora', fontsize=12)
    ax2.set_ylabel('Volume (BTC)', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Rotacionar datas
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    
    plt.tight_layout()
    plt.show()