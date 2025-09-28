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




from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import SPOT_REST_API_PROD_URL
from binance_sdk_spot.spot import Spot
from binance_sdk_spot.rest_api.models import ExchangeInfoResponse, RateLimits

logging.basicConfig(level=logging.INFO)
configuration = ConfigurationRestAPI(api_key="your-api-key", api_secret="your-api-secret", base_path=SPOT_REST_API_PROD_URL)

client = Spot(config_rest_api=configuration)

try:
    response = client.rest_api.exchange_info(symbol="BNBUSDT")

    rate_limits: List[RateLimits] = response.rate_limits
    logging.info(f"exchange_info() rate limits: {rate_limits}")

    data: ExchangeInfoResponse = response.data()
    logging.info(f"exchange_info() response: {data}")
except Exception as e:
    logging.error(f"exchange_info() error: {e}")
