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
    - After creating the api_key, you must edit it, inserting your public IP and allowing trading spot
    (you'll find your public IP in https://whatismyipaddress.com/)

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

from rest_api.config import rest_client
from rest_api.filter import Filter
from rest_api.error_handling import error_handler


@error_handler
def main():
    'main function'
    account_info = rest_client.rest_api.get_account()
    print(account_info)

if __name__ == "__main__":
    main()
