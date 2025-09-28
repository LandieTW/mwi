
import json
import os

from rest_api.certificate_pinning import ssl_context

from binance_common.constants import TimeUnit
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_spot.spot import Spot

api_keys_path = os.path.join(os.path.dirname(__file__), '../api_keys.json')
try:
    with open(api_keys_path, 'r', encoding='utf-8') as file:
        keys = json.load(file)
        my_api_key = keys['my_api_key']
        my_secret_key = keys['my_secret_key']
except FileNotFoundError:
    raise FileNotFoundError(f"API keys file not found at {api_keys_path}. \
                            Please create the file with your API keys.")

config_rest_api = ConfigurationRestAPI(
    api_key=my_api_key,                         # my_api_key
    api_secret = my_secret_key,                 # my_secret_key
    base_path = None,
    timeout = 1000,                             # Request timeout in milliseconds
    proxy = None,
    keep_alive = True,                          # Enable Keep-Alive
    compression = True,                         # Enable response compression
    retries = 3,                                # Number of retry attempts for failed requests
    backoff = 1000,                             # Delay (ms) between retries
    https_agent = ssl_context,                  # Custom HTTPS Agent with certificate pinning  
    time_unit = TimeUnit.MILLISECOND.value,     # Time unit for time-based responses
    private_key = None,
    private_key_passphrase = None,
    custom_headers = {},                        # Custom REST headers
    )

rest_client = Spot(
    config_rest_api = config_rest_api,
    config_ws_api = None,
    config_ws_streams = None,
    )
