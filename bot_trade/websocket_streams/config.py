
from binance_common.configuration import ConfigurationWebSocketStreams
from binance_common.constants import SPOT_WS_STREAMS_PROD_URL
from binance_common.constants import WebsocketMode


config_websocket_streams = ConfigurationWebSocketStreams(
    reconnect_delay = 5,
    compression = 0,
    proxy = None,
    mode = WebsocketMode.SINGLE,
    pool_size = 2,
    time_unit = None,
    https_agent = None,
    stream_url=SPOT_WS_STREAMS_PROD_URL,
)
