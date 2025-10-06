"""
Descritpion:
    - This is a sample code to start trading with Binance Spot API using the binance-sdk-spot package.
    - Python connector - https://github.com/binance/binance-connector-python
    
    ---------------------------------------------
    ------------- REST API ----------------------
    ---------------------------------------------

    Characteristics:
        Synchronous communication (request-response)
        HTTP/HTTPS protocol
        Stateless - each request is independent
        Ideal for specific operations

    Use cases:
        Get account information
        Place orders (buy/sell)
        Check balances
        Retrieve historical data

    ---------------------------------------------
    ------------- WEBSOCKET API -----------------
    ---------------------------------------------
    
    Characteristics:
        Asynchronous and bidirectional communication
        Persistent connection
        Stateful - maintains connection state
        Ideal for receiving real-time data

    Use cases:
        Receive ticker updates
        Monitor market depth (order book)
        Receive real-time trade data

    ---------------------------------------------
    ------------- WEBSOCKET STREAM --------------
    ---------------------------------------------
    
    Characteristics:
        Subset of WebSocket API
        Focused only on receiving data (streaming)
        Doesn't send commands to the server
        Optimized for continuous data flow

    --------------------------------------------------------------------------------
    ---------------- REST API x WEBSOCKET API x WEBSOCKET STREAM -------------------
    --------------------------------------------------------------------------------
    Characteristic	    REST API	        WebSocket API	    WebSocket Stream
    Direction	        Client → Server	    Bidirectional	    Server → Client
    Connection	        Temporary	        Persistent	        Persistent
    Latency	            High	            Low	                Very Low
    Usage	            Actions	            Commands + Data	    Data Only
    Complexity	        Low	                High	            Medium

    
Necessary
    - Python (version 3.9 or later)
    - pip (Python package manager)
    - poetry (Python package manager)

In Binance
    - You must have an acoount on Binance
    - You should create your own api_key in API Manager
    - When creating the api_key, remember to get the secret_key
    (that's available to be copied just in the moment of creation of the api_key)
    - After creating the api_key, you must edit it, inserting your public IP and allowing 
    trading spot (you'll find your public IP in https://whatismyipaddress.com/)

Use on CMD
    - Installing Binance SDK Spot (pip install binance-sdk-spot)
    - Installing pipx (py -m pip install --user pipx)
    - Ensuring pipx's path (On a new terminal: py -m pipx ensurepath)
    - Installing poetry (pipx install poetry)
    - pip install pyopenssl
"""


import time

from rest_api.rest_api_config import client_rest
from websocket_api.websocket_api_config import client_ws_api
from websocket_streams.websocket_streams_config import client_ws_streams

from rest_api import error_handling, filter

from rest_api.functions import (rest_api_account, rest_api_general, rest_api_market, 
    rest_api_trade, rest_api_user_data_stream)
from websocket_api.functions import (websocket_api_account, auth, websocket_api_general, 
    websocket_api_market, websocket_api_trade, websocket_api_user_data_stream)
from websocket_streams.functions import (websocket_streams_functions)

from websocket_api.websocket_api_agent import call_exchange_info
from websocket_streams.websocket_streams_agent import call_agg_trade


class MyCount:
    def __init__(self,):
        self.client = client_rest
        self.info = rest_api_account.get_account(client=self.client, omit_zero_balances=True)['data']
        self.symbol = 'BTCUSDT'
        self.end_time = int(time.time() * 1_000)
        self.start_time = self.end_time - (30 * 24 * 60 * 60 * 1_000)
        self.tax = self.calculate_taxes(client=self.client)
        '''
        self.incomes = self.check_my_trades(client=self.client)
        '''

    def calculate_taxes(self) -> float:
        '''
        Calculate taxes rate for each order
        '''
        comission_data = rest_api_account.account_comission(client=self.client, symbol=self.symbol)['data']
        # calculate taxes
        taxes = eval(comission_data.standard_commission.taker) + eval(comission_data.special_commission.taker) + eval(comission_data.tax_commission.taker)
        # calculate discount
        discount_taxes = comission_data.discount.discount if (self.check_coin_in_account(coin=comission_data.discount.discount_asset) and comission_data.discount.enabled_for_account) else 0
        return taxes * (1-discount_taxes)
        

    def check_coin_in_account(self, coin: str) -> bool:
        '''
        Check if the coin is in account.
        '''
        balances = self.info.balances
        bnb_balance = next((balance for balance in balances if coin.lower() in balance.asset.lower()), None)
        return True if eval(bnb_balance.free) > .1 else False


    def get_order_id(self):
        '''
        Get order id from XX days ago
        '''
        params = {
            'client': self.client,
            'symbol': self.symbol,
            'order_id': None,
            'start_time': self.start_time,
            'end_time': None,
            'limit': 1_000,
            'recv_window': None
        }
        orders_id = rest_api_account.all_orders(**params)['data']
        oldest_order_id = min(orders_id, key=lambda x: x['time'])
        return oldest_order_id.orderId


    def check_my_trades(self):
        '''
        Check my trades data
        '''
        params = {
            'client': self.client,
            'symbol': self.symbol,
            'order_id': None,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'from_id': self.get_order_id(client=self.client),
            'limit': None,
            'recv_window': None
        }
        trade_data = rest_api_account.my_trades(**params)['data']

        print('HERE')



@error_handling.error_handler
def main():
    """
    Description:

    """
    my_count = MyCount()




    print('HERE')




if __name__ == "__main__":
    main()
