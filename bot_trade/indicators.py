
import pandas as pd
import numpy as np


# ----------------------------------------------------------------------------------
# TREND INDICATORS -----------------------------------------------------------------
# ----------------------------------------------------------------------------------


# Considera geometria fractal para uma tripla suavização na perseguição do preço
def frama(
        df: pd.DataFrame,
        n: int = 14
    ) -> pd.DataFrame:
    """
    Description:
        Fractals Adaptive Moving Average
            1. Calculates the Mean Prices
            2. Calculates the fractals lengths
            3. Calculates D (Fractal Dimension)
            4. Calculates the Adaptive Coefficient
            5. Calculates FRAMA
    How to use:
        It's a moving average that adapts itself with fractals parameters
    Parameters:
        df. Dataframe with market data
        n. Periods used to build the indicator
    Returns:
        df. Dataframe with the new indicator
    """
    # 1. Preço médio
    price = (df['high'] + df['low']) / 2
    # 2. Calcular N1, N2, N3
    N1 = (df['high'].rolling(window=n).max() - 
          df['low'].rolling(window=n).min())
    N2 = (df['high'].rolling(window=n//2).max() - 
          df['low'].rolling(window=n//2).min())
    N3 = (df['high'].shift(n//2).rolling(window=n//2).max() - 
          df['low'].shift(n//2).rolling(window=n//2).min())
    # 3. Dimensão Fractal (D)
    denominator = (N2 + N3)
    D = np.where(
        (denominator > 0) & (N1 > 0),
        (np.log(N1) - np.log(denominator / 2)) / np.log(2),
        1.0
    )
    D = np.clip(D, 1.0, 2.0)
    # 4. Coeficiente Adaptativo (Alpha)
    alpha = np.exp(-4.6 * (D - 1))
    alpha = np.clip(alpha, 0.01, 1.0)
    # 5. Calcular FRAMA iterativamente
    frama_values = []
    frama_current = price.iloc[0]
    for i in range(len(df)):
        if pd.isna(alpha[i]) or pd.isna(price.iloc[i]):
            frama_values.append(np.nan)
        else:
            frama_current = alpha[i] * price.iloc[i] + (1 - alpha[i]) * frama_current
            frama_values.append(frama_current)
    df['FRAMA'] = frama_values
    return df


# Indica Força da tendência
def adx(
        df: pd.DataFrame,
        n: int = 14,
        wilder: bool = False
    ) -> pd.DataFrame:
    """
    Description:
        Average Directional Movement Index
            1. Calculates the TR (True Range)
            2. Calculates the DM (Directional Movement)
            3. Smoothing the values
            4. Calculates the DI (Directional Indicatores)
            5. Calculates the DX (Directional Index)
            6. Calculates the ADX (Average Directional Index)
    How to use:
        ADX
            ADX < 20 - Weak Trend
            20 < ADX < 25 - Possible Trend
            25 < ADX < 50 - Strong Trend
            50 < ADX - Very Strong Trend
            70 < ADX - Exhausted Trend
        +DI and -DI
            +DI > -DI - Bullish
            +DI < -DI - Bearish
            +DI = -DI - Signals a change in trend
    Parameters:
        df. Dataframe with market data
        n. Periods used to build the indicator
        wilder. Smooths even more the signals
    Returns:
        df. Dataframe with the new indicator
    """
    # True Range (TR)
    df['TR'] = pd.concat(
        [
            abs(df['high'] - df['low']),
            abs(df['high'] - df['close'].shift(1)),
            abs(df['low'] - df['close'].shift(1))
        ],
        axis=1
    ).max(axis=1)
    # Directional Movement (DM) - CORREÇÃO DA LÓGICA
    high_diff = df['high'] - df['high'].shift(1)
    low_diff = df['low'].shift(1) - df['low']
    df['+DM'] = np.where(
        (high_diff > low_diff) & (high_diff > 0),
        high_diff,
        0
    )
    df['-DM'] = np.where(
        (low_diff > high_diff) & (low_diff > 0),
        low_diff,
        0
    )
    # Smoothing the values - CORREÇÃO COMPLETA
    if wilder:
        # Wilder smoothing (EMA-like)
        df['Smoothed_TR'] = df['TR'].ewm(alpha=1/n, adjust=False).mean()
        df['Smoothed_+DM'] = df['+DM'].ewm(alpha=1/n, adjust=False).mean()
        df['Smoothed_-DM'] = df['-DM'].ewm(alpha=1/n, adjust=False).mean()
    else:
        # Standard smoothing (SMA)
        df['Smoothed_TR'] = df['TR'].rolling(window=n).mean()
        df['Smoothed_+DM'] = df['+DM'].rolling(window=n).mean()
        df['Smoothed_-DM'] = df['-DM'].rolling(window=n).mean()
    # Directional Indicators (DI) - CORREÇÃO DO NOME
    df['+DI'] = (df['Smoothed_+DM'] / df['Smoothed_TR']) * 100
    df['-DI'] = (df['Smoothed_-DM'] / df['Smoothed_TR']) * 100
    # Directional Index (DX)
    df['DX'] = (abs(df['+DI'] - df['-DI']) / (df['+DI'] + df['-DI'])) * 100
    # Average Directional Index (ADX) - CORREÇÃO
    if wilder:
        df['ADX'] = df['DX'].ewm(alpha=1/n, adjust=False).mean()
    else:
        df['ADX'] = df['DX'].rolling(window=n).mean()
    df = df.drop(columns=['TR', '+DM', '-DM', 'Smoothed_TR', 'Smoothed_+DM', 'Smoothed_-DM', 'DX'])
    return df


# Indica volatilidade e possíveis pontos de reversão
def bb(
        df: pd.DataFrame,
        n: int = 20,
        k: int = 2
    ) -> pd.DataFrame:
    """
    Description:
        Bollinger Bands
            1. Mean band
            2. Standard deviation bands
    How To Use:
        The bands countains ~95% of the prices
        A touch in a band is not necessarily a buy/sell signal
        Movements usually goes from a band to the other
        Squeeze bands precedes large bands (and vice versa)
    Parameters:
        df. Dataframe with market data
        n. Periods used to build the indicator
        k. Standard deviations used to build the bands
    Returns:
        df. Dataframe with the new indicator
    """
    # Mean Band (SMA)
    df['BB_Mean'] = df['close'].rolling(window=n).mean()
    # Standard Deviation
    std = df['close'].rolling(window=n).std()
    # Bands
    df['BB_Upper'] = df['BB_Mean'] + (k * std)
    df['BB_Lower'] = df['BB_Mean'] - (k * std)
    return df


# Indicador de tendência completo
def ikh(
        df: pd.DataFrame,
        tenkan_sen: int = 9,
        kijun_sen: int = 26,
        senkou_span_b: int = 52,
        displacement: int = 26
    ) -> pd.DataFrame:
    """
    Description
        Ichimoku Kinko Hyo
            1. tenkan_sen - Conversion line
            2. kijun_sen - Base line
            3. senkou_span_a - Leading span A
            4. senkou_span_b - Leading span B
            5. chikou span - Lagging span
            6. kumo - Cloud
    How to use:
        Tenkan - Where the price is
        Kijun - Where the price goes
        Senkou A - Superior Cloud band (Supoorts/Resistances)
        Senkou B - Inferior Cloud band (Supoorts/Resistances)
        Chikou - From where the price comes
        Kumo - Buy/Sell Signals
        Kumo width squeeze - Weak Support/Resistance
        Kumo width large - Strong Support/Resistance
    Parameters:
    Returns:
    """
    # tenkan sen
    df = frama(df, n=tenkan_sen)
    df['tenkan'] = df['FRAMA']
    # df['tenkan'] = (df['high'].rolling(tenkan_sen).max() +\
    #                 df['low'].rolling(tenkan_sen).min()) / 2
    # kijun sen
    df['kijun'] = (df['high'].rolling(kijun_sen).max() +\
                    df['low'].rolling(kijun_sen).min()) / 2
    # chikou span
    df['chikou'] = df['close'].shift(-displacement)
    # senkou span a
    df['senkou A'] = ((df['tenkan'] + df['kijun']) / 2).shift(displacement)
    # senkou span b
    df['senkou B'] = ((df['high'].rolling(senkou_span_b).max() +\
                        df['low'].rolling(senkou_span_b).min()) / 2
                        ).shift(displacement)
    # kumo
    df['kumo_top'] = df[['senkou A', 'senkou B']].max(axis=1)
    df['kumo_bottom'] = df[['senkou A', 'senkou B']].min(axis=1)

    # SIGNALS

    # bandas abertas da nuvem indicam tendência forte
    if df['kumo_top'].iloc[-1] == df['senkou A'].iloc[-1]:
        # banda superior da nuvem indica crescimento futuro
        if df['kumo_top'].iloc[-1] == df['senkou A'].iloc[-1]:
            trend_1 = "bullish"            
        # banda inferior da nuvem indica queda futura
        elif df['kumo_top'].iloc[-1] == df['senkou B'].iloc[-1]:
            trend_1 = "bearish"
    # bandas fechadas da nuvem indicam tendência fraca
    else:
        trend_1 = "sideways"

    # médias móveis indicam tendência de alta
    if df['tenkan'].iloc[-1] > df['kijun'].iloc[-1] and\
        df['tenkan'].iloc[-1] > df['kumo_top'].iloc[-1] and\
            df['kijun'].iloc[-1] > df['kumo_top'].iloc[-1]:
        trend_2 = "bullish"
    # médias móveis indicam tendência de baixa
    elif df['tenkan'].iloc[-1] < df['kijun'].iloc[-1] and\
        df['tenkan'].iloc[-1] < df['kumo_bottom'].iloc[-1] and\
            df['kijun'].iloc[-1] < df['kumo_bottom'].iloc[-1]:
        trend_2 = "bearish"
    # médias móveis indicam tendência lateral
    else:
        trend_2 = "sideways"
    
    # chikou maior que o preço passado indica tendência de alta
    if df['chikou'].iloc[-27] > df['close'].iloc[-27]:
        trend_3 = "bullish"
    # chikou menor que o preço passado indica tendência de baixa
    elif df['chikou'].iloc[-27] < df['close'].iloc[-27]:
        trend_3 = "bearish"
    # chikou igual ao preço passado indica tendência lateral
    else:
        trend_3 = "sideways"

    if trend_1 == "bullish" and trend_2 == "bullish" and trend_3 == "bullish":
        signal = True
        trend = "bullish"
    elif trend_1 == 'bearish' and trend_2 == 'bearish' and trend_3 == 'bearish':
        signal = True
        trend = "bearish"
    else:
        signal = False
        trend = "sideways"

    df['ikh_signal'] = [np.nan] * (len(df) - 1) + [signal]
    df['ikh_trend'] = [np.nan] * (len(df) - 1) + [trend]

    df = df.drop(columns=['FRAMA', 'tenkan', 'kijun', 'chikou',
                          'senkou A', 'senkou B', 'kumo_top', 'kumo_bottom'])

    return df


# Segue o preço baseado na tendência
def p_sar(
        df: pd.DataFrame,
        acceleration: float = 0.02,
        maximum: float = 0.2
    ) -> pd.DataFrame:
    """
    Description:
        Parabolic Stop and Reverse
    How to use:
        Points below the price - Bullish trend
        Points above the price - Bearish trend  
        Flip when price crosses the SAR
    Parameters:
        df. Dataframe with market data
        acceleration. Acceleration factor
        maximum. Maximum acceleration
    Returns:
        df. Dataframe with the new indicator
    """
    high = df['high'].values
    low = df['low'].values
    sar_arr = np.full(len(df), np.nan)
    trend = 1  # 1: uptrend, -1: downtrend
    ep = high[0]  # Extreme point
    af = acceleration  # Acceleration factor
    sar_arr[0] = low[0]  # Initial SAR
    for i in range(1, len(df)):
        prev_sar = sar_arr[i-1]
        if trend == 1:
            # Uptrend logic
            sar_arr[i] = prev_sar + af * (ep - prev_sar)
            # Reverse if low breaks SAR
            if low[i] < sar_arr[i]:
                trend = -1
                sar_arr[i] = ep
                ep = low[i]
                af = acceleration
            else:
                # Update extreme point and acceleration
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + acceleration, maximum)
                # SAR should not be above last two lows
                sar_arr[i] = min(sar_arr[i], low[i-1])
                if i > 1:
                    sar_arr[i] = min(sar_arr[i], low[i-2])
        else:
            # Downtrend logic
            sar_arr[i] = prev_sar - af * (prev_sar - ep)
            # Reverse if high breaks SAR
            if high[i] > sar_arr[i]:
                trend = 1
                sar_arr[i] = ep
                ep = high[i]
                af = acceleration
            else:
                # Update extreme point and acceleration
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + acceleration, maximum)
                # SAR should not be below last two highs
                sar_arr[i] = max(sar_arr[i], high[i-1])
                if i > 1:
                    sar_arr[i] = max(sar_arr[i], high[i-2])
    df['SAR'] = sar_arr
    return df


# ----------------------------------------------------------------------------------
# VOLATILITY INDICATORS ------------------------------------------------------------
# ----------------------------------------------------------------------------------


# Indica a volatilidade do mercado
def atr(
        df: pd.DataFrame,
        n: int = 14
    ) -> pd.DataFrame:
    """
    Description:
        Average True Range
    How to use:
        High ATR means high volatility
        Low ATR means calm market
    Parameters:
        df. Dataframe with market data
        n. Periods used to build the indicator
    Returns:
        df. Dataframe with the new indicator
    """
    tr1 = df['high'] - df['low']
    tr2 = (df['high'] - df['close'].shift(1)).abs()
    tr3 = (df['low'] - df['close'].shift(1)).abs()
    df['TR'] = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    # Wilder's smoothing (equivalente a uma EMA com alpha = 1/n)
    df['ATR'] = df['TR'].ewm(alpha=1/n, adjust=False).mean()
    df = df.drop(columns=['TR'])
    return df


# Indica pontos de sobre-compra ou sobre-venda
def chaikin(
        df: pd.DataFrame,
        short: int = 3,
        long: int = 10
    ) -> pd.DataFrame:
    """
    Description:
        Chaikin Oscillator
    How to use:
        High Chaikin Oscillator means bullish trend
        Low Chaikin Oscillator means bearish trend
    Parameters:
        df. Dataframe with market data
        short. Short period for EMA
        long. Long period for EMA
    Returns:
        df. Dataframe with the new indicator
    """
    # Evitar divisão por zero
    hl_range = df['high'] - df['low']
    hl_range = hl_range.replace(0, np.nan)
    # Close Location Value (CLV)
    clv = ((df['close'] - df['low']) - (df['high'] - df['close'])) / hl_range
    # Linha de Acumulação/Distribuição (ADL)
    adl = (clv * df['volume']).cumsum()
    # Chaikin Oscillator = EMA_short(ADL) - EMA_long(ADL)
    ema_short = adl.ewm(span=short, adjust=False).mean()
    ema_long = adl.ewm(span=long, adjust=False).mean()
    df['ChaikinOsc'] = ema_short - ema_long
    return df

