
from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import SPOT_WS_STREAMS_PROD_URL
from binance_common.constants import WebsocketMode
from binance_common.constants import TimeUnit
from binance_sdk_spot.spot import Spot


config_websocket_streams = ConfigurationWebSocketStreams(
    reconnect_delay = 5000,
    compression = 0,
    proxy = None,
    mode = WebsocketMode.POOL,
    pool_size = 3,
    time_unit = TimeUnit.MILLISECOND.value,
    https_agent = None,
    stream_url=SPOT_WS_STREAMS_PROD_URL,
)


client_ws_streams = Spot(
    config_ws_streams = config_websocket_streams,
    )
