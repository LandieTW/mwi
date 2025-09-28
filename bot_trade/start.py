"""
Descritpion:
    - This is a sample code to start trading with Binance Spot API using the binance-sdk-spot package.
    - Python connector - https://github.com/binance/binance-connector-python

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

from filter import Filter
from certificate_pinning import ssl_context

from binance_common.configuration import ConfigurationRestAPI
from binance_common.constants import SPOT_REST_API_PROD_URL
from binance_sdk_spot.rest_api.models import ExchangeInfoResponse, RateLimits
from binance_sdk_spot.spot import Spot

my_api_key = r'ASAZ6e17Ps3J74RARr1uwCp88LWJiutEzIY4e4GSyt5391IXy5QqoXZ8ruG0jsGn'
my_secret_key = r'3pUwRYRoVrbhCcWAlcPAqr3XzYrqlmbjY86WCWmVpmnhdE5HoxlpDAXaNGk3ZSL2'

config_rest_api = ConfigurationRestAPI(
    api_key=my_api_key,                     # my_api_key
    api_secret = my_secret_key,             # my_secret_key
    base_path = None,
    timeout = 1000,                         # Request timeout in milliseconds
    proxy = None,
    keep_alive = True,                      # Enable Keep-Alive
    compression = True,                     # Enable response compression
    retries = 3,                            # Number of retry attempts for failed requests
    backoff = 1000,                         # Delay (ms) between retries
    https_agent = ssl_context,              # Custom HTTPS Agent with certificate pinning  
    time_unit = None,
    private_key = None,
    private_key_passphrase = None,
    custom_headers = {},                    # Custom REST headers
    )

client = Spot(
    config_rest_api = config_rest_api,
    config_ws_api = None,
    config_ws_streams = None,
    )

'testing'
account_info = client.rest_api.get_account()
print(account_info)


