
from others.api_keys import my_api_key
from others.api_keys import my_secret_key

from binance_common.configuration import ConfigurationWebSocketAPI
from binance_common.constants import SPOT_WS_API_PROD_URL
from binance_common.constants import WebsocketMode


config_websocket_api = ConfigurationWebSocketAPI( 
    api_key = my_api_key,
    api_secret = my_secret_key,
    private_key = None,
    private_key_passphrase = None,
    stream_url = SPOT_WS_API_PROD_URL,
    timeout = 5,
    reconnect_delay = 5,
    compression = 0,
    proxy = None,
    mode = WebsocketMode.SINGLE,
    pool_size = 2,
    time_unit = None,
    https_agent = None,
    session_re_logon = True,
    )
