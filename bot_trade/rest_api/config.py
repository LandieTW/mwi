
from others.api_keys import my_api_key
from others.api_keys import my_secret_key
from rest_api.certificate_pinning import ssl_context

from binance_common.constants import TimeUnit
from binance_common.configuration import ConfigurationRestAPI

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
