import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graph_plot(df, title="Financial Chart", figsize=(12, 10)):
    """
    Gera um gráfico financeiro com múltiplos indicadores técnicos.
    
    O gráfico é composto por:
    - Preço + indicadores sobrepostos (Ichimoku, Bollinger, etc.)
    - Subgráficos separados para indicadores específicos (ADX, RSI, MACD, etc.)
    - Volume
    
    Parâmetros
    ----------
    df : pandas.DataFrame
        DataFrame contendo colunas como ['open_time', 'open', 'high', 'low', 'close', 'volume', ...]
    title : str, opcional
        Título principal do gráfico
    figsize : tuple, opcional
        Tamanho da figura
    """
    
    # ===============================================================
    # Configuração de quais indicadores pertencem a cada grupo
    # ===============================================================
    price_indicators = [
        'FRAMA', 
        'TEMA', 
        'VIDA', 
        'BB_Upper', 'BB_Lower', 'BB_Mean', 
        'tenkan', 'kijun', 'chikou', 'kumo_top', 'kumo_bottom',
        'SAR',
        'Jaw', 'Teeth', 'Lips'
    ]
    
    separate_indicators = {
        'ADX': ['+DI', '-DI', 'ADX'],
        'ATR': ['ATR'],
        'ChaikinOsc': ['ChaikinOsc'],
        'AC': ['AC']
    }
    
    # ===============================================================
    # Preparação dos dados
    # ===============================================================
    basic_columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 
                     'close_time', 'taker_buy_base_volume']
    
    df = df.copy()
    indicadores = [col for col in df.columns if col not in basic_columns and col != 'index']
    
    # Converter datas
    if 'open_time' in df.columns:
        try:
            x = pd.to_datetime(df['open_time'], unit='us')
            x_label = 'Time'
        except Exception:
            x = range(len(df))
            x_label = 'Periods'
    else:
        x = range(len(df))
        x_label = 'Periods'
    
    # ===============================================================
    # Detectar quais indicadores separados estão presentes
    # ===============================================================
    active_separate_indicators = {
        name: [col for col in cols if col in indicadores]
        for name, cols in separate_indicators.items()
        if any(col in indicadores for col in cols)
    }
    
    n_subplots = 2 + len(active_separate_indicators)  # preço + volume + extras
    
    height_ratios = [3] + [1] * (n_subplots - 1)
    fig, axes = plt.subplots(n_subplots, 1, figsize=figsize, gridspec_kw={'height_ratios': height_ratios})
    
    if n_subplots == 1:
        axes = [axes]
    
    ax_price = axes[0]
    ax_volume = axes[1]
    extra_axes = axes[2:] if len(axes) > 2 else []
    
    # ===============================================================
    # Plot principal: preço + indicadores sobrepostos
    # ===============================================================
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray',
              'cyan', 'magenta', 'yellow', 'lime', 'teal', 'coral', 'navy', 'maroon',
              'olive', 'skyblue', 'salmon', 'gold', 'darkgreen', 'royalblue', 'crimson',
              'darkorange', 'mediumpurple', 'chocolate', 'steelblue', 'seagreen']
    
    if 'kumo_top' in df.columns and 'kumo_bottom' in df.columns:
        ax_price.fill_between(x, df['kumo_top'], df['kumo_bottom'], 
                              alpha=0.2, color='gray', label='Kumo Cloud')
    
    ax_price.plot(x, df['close'], color='black', linewidth=2, label='Close Price')
    
    active_price_indicators = [ind for ind in price_indicators if ind in indicadores]
    
    for i, ind in enumerate(active_price_indicators):
        color = colors[i % len(colors)]
        
        if ind == 'SAR':
            ax_price.plot(x, df[ind], marker='o', markersize=2, color=color,
                          linewidth=0, label=ind, alpha=0.8)
        else:
            ax_price.plot(x, df[ind], color=color, linewidth=1.5, label=ind, alpha=0.8)
    
    ax_price.set_title(f'{title} - Price and Indicators', fontweight='bold')
    ax_price.set_ylabel('Price')
    ax_price.legend()
    ax_price.grid(True, alpha=0.3)
    
    # ===============================================================
    # Volume
    # ===============================================================
    if 'volume' in df.columns:
        ax_volume.plot(x, df['volume'], color='purple', linewidth=1, label='Volume', alpha=0.8)
        ax_volume.set_title('Volume', fontweight='bold')
        ax_volume.set_ylabel('Volume')
        ax_volume.legend()
        ax_volume.grid(True, alpha=0.3)
    
    # ===============================================================
    # Indicadores separados
    # ===============================================================
    for ax, (name, cols) in zip(extra_axes, active_separate_indicators.items()):
        for i, col in enumerate(cols):
            color = colors[i % len(colors)]
            ax.plot(x, df[col], color=color, linewidth=1.5, label=col, alpha=0.8)
        
        # Ajustes específicos para alguns indicadores
        if name == 'ADX':
            ax.axhline(y=20, color='gray', linestyle='--', alpha=0.3)
            ax.axhline(y=25, color='gray', linestyle='--', alpha=0.3)
            ax.axhline(y=50, color='gray', linestyle='--', alpha=0.3)
            ax.set_ylim(0, 100)
        
        if name == 'RSI':
            ax.axhline(y=30, color='gray', linestyle='--', alpha=0.3)
            ax.axhline(y=70, color='gray', linestyle='--', alpha=0.3)
            ax.set_ylim(0, 100)
        
        ax.set_title(name, fontweight='bold')
        ax.set_ylabel(name)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    # ===============================================================
    # Eixos e layout
    # ===============================================================
    axes[-1].set_xlabel(x_label)
    if x_label == 'Time':
        for ax in fig.axes:
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
    
    plt.tight_layout()
    return fig, axes
