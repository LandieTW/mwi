
import os
from others.api_keys import my_api_key, my_secret_key
from rest_api.certificate_pinning import ssl_context
from binance_common.configuration import ConfigurationRestAPI
from binance_sdk_spot.spot import SPOT_REST_API_PROD_URL

config_rest_api = ConfigurationRestAPI(
    api_key=my_api_key,
    api_secret = my_secret_key,
    base_path = os.getenv("BASE_PATH", SPOT_REST_API_PROD_URL),
    https_agent = ssl_context,
    )
