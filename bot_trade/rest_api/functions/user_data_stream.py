
from typing import Union
from bot_trade.others.functions import get_data
from collections import defaultdict
from binance_sdk_spot.spot import Spot


def put_user_data_stream(
        client: Spot,
        listen_key: Union[str, None],
    ) -> defaultdict:
    """
    Description:
        Keepalive a user data stream to prevent a time out. User data streams will close 
        after 60 minutes. 
        It's recommended to send a ping about every 30 minutes.
    """
    return get_data(
        client.rest_api.put_user_data_stream(
            listen_key=listen_key
        )
    )

def new_user_data_stream(
        client: Spot,
    ) -> defaultdict:
    """
    Description:
        Start a new user data stream.
        The stream will close after 60 minutes unless a keepalive is sent.
    """
    return get_data(
        client.rest_api.new_user_data_stream()
    )

def delete_user_data_stream(
        client: Spot,
        listen_key: Union[str, None],
    ) -> defaultdict:
    """
    Description:
         Close out a user data stream.
    """
    return get_data(
        client.rest_api.delete_user_data_stream(
            listen_key=listen_key
        )
    )
