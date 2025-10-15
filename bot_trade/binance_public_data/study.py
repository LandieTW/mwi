
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob
import os
from graph import graph_plot
import indicators


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
    
    data = binance_data_path[0]

    # loading data as a DataFrame
    df = pd.read_csv(data, names=columns)

    df = df.drop(columns=['ignore', 'quote_volume', 'taker_buy_quote_volume', 'trades'])

    df = indicators.ikh(df)

    df_plot = df.tail(100).reset_index()

    fig, axes = graph_plot(df_plot)
    plt.show()

    print('HERE')



if __name__ == "__main__":
    main()

