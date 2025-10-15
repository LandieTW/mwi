
import os
from binance_common.constants import WebsocketMode
from binance_common.constants import TimeUnit
from binance_sdk_spot.spot import Spot, ConfigurationWebSocketStreams, SPOT_WS_STREAMS_PROD_URL


config_websocket_streams = ConfigurationWebSocketStreams(
    stream_url=os.getenv("STREAM_URL", SPOT_WS_STREAMS_PROD_URL),
)


client_ws_streams = Spot(
    config_ws_streams = config_websocket_streams,
    )
