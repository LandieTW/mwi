"""
Descritpion:
    - This is a sample code to start trading with Binance Spot API using the binance-sdk-spot
    package.
    - Python connector - https://github.com/binance/binance-connector-python
    - Bynance public data - https://data.binance.vision/
    
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


import asyncio
from rest_api_config import client_rest
# from websocket_api.websocket_api_config import client_ws_api
from websocket_streams_config import client_ws_streams
import error_handling
import rest_api_classes
import websocket_streams_classes


@error_handling.error_handler
def main():
    """
    Description:

    """


    analysis_kline = websocket_streams_classes.KlineAnalysis(client_ws_streams, client_rest)
    asyncio.run(analysis_kline.gather_routines())
    
    my_count = rest_api_classes.MyCount(client=client_rest)

    print("HERE")
    

if __name__ == "__main__":
    main()

