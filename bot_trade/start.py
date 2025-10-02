"""
Descritpion:
    - This is a sample code to start trading with Binance Spot API using the binance-sdk-spot package.
    - Python connector - https://github.com/binance/binance-connector-python
    - Use rest_api to get static data
    - Use websocket_api to trade in real time
    - Use websocket_streams to get real time data
    
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

About future trading
    - https://www.binance.com/en/support/faq/detail/360039304272
    - https://developers.binance.com/docs/derivatives/quick-start
"""


from rest_api.config import config_rest_api
from websocket_api.config import config_websocket_api
from websocket_streams.config import config_websocket_streams

from rest_api.filter import Filter
from rest_api.error_handling import error_handler
from rest_api.functions import account
from rest_api.functions import genneral
from rest_api.functions import market
from rest_api.functions import trade

from websocket_api.agent import call_exchange_info
from websocket_streams.agent import call_agg_trade

from binance_sdk_spot.spot import Spot


@error_handler
def main():
    """
    Description:

    """
    client = Spot(
        config_rest_api = config_rest_api,
        config_ws_api = config_websocket_api,
        config_ws_streams = config_websocket_streams,
        )
    


if __name__ == "__main__":
    main()


