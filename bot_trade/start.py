"""
Descritpion:
    - This is a sample code to start trading with Binance Spot API using the binance-sdk-spot package.

Necessary
    - Python (version 3.9 or later)
    - pip (Python package manager)
    - poetry (Python package manager)

Use on CMD
    - Installing Binance SDK Spot (pip install binance-sdk-spot)
    - Installing pipx (py -m pip install --user pipx)
    - Ensuring pipx's path (On a new terminal: py -m pipx ensurepath)
    - Installing poetry (pipx install poetry)
"""


from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_spot.spot import Spot

my_api_key = 'ASAZ6e17Ps3J74RARr1uwCp88LWJiutEzIY4e4GSyt5391IXy5QqoXZ8ruG0jsGn'

config_rest_api = ConfigurationRestAPI(
    api_key=my_api_key,     # my_api_key
    api_secret = None,
    base_path = None,
    timeout = 1000,
    proxy = None,
    keep_alive = True,
    compression = True,
    retries = 3,
    backoff = 1000,
    https_agent = None,
    time_unit = None,
    private_key = None,
    private_key_passphrase = None,
    custom_headers = {},
    )

client = Spot(
    config_rest_api = config_rest_api,
    config_ws_api = None,
    config_ws_streams = None,
    )

account_info = client.rest_api.get_account()
