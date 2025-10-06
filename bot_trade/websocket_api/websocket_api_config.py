
from others.api_keys import my_api_key, my_secret_key
from binance_common.configuration import ConfigurationWebSocketAPI
from binance_common.constants import SPOT_WS_API_PROD_URL, WebsocketMode
from binance_sdk_spot.spot import Spot


config_websocket_api = ConfigurationWebSocketAPI( 
    api_key = my_api_key,
    api_secret = my_secret_key,
    stream_url = SPOT_WS_API_PROD_URL,
    mode = WebsocketMode.POOL,
    pool_size = 3,
    )


client_ws_api = Spot(
    config_ws_api = config_websocket_api,
    )