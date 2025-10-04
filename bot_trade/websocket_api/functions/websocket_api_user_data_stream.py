
import asyncio
from typing import Optional, Union
from others.other_functions import get_data
from collections import defaultdict
from binance_sdk_spot.spot import Spot


async def user_data_stream_unsubscribe(
        client: Spot,
        id: Optional[str] = None,
        subscription_id: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Stop listening to the User Data Stream in the current WebSocket connection.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.user_data_stream_unsubscribe(
            id=id,
            subscription_id=subscription_id
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_user_data_stream_unsubscribe(
        client: Spot,
        id: Optional[str] = None,
        subscription_id: Optional[int] = None,
    ):
    asyncio.run(
        user_data_stream_unsubscribe(
            client=client,
            id=id,
            subscription_id=subscription_id
        )
    )


async def user_data_stream_subscribe(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Subscribe to the User Data Stream in the current WebSocket connection.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.user_data_stream_subscribe(
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_user_data_stream_subscribe(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        user_data_stream_subscribe(
            client=client,
            id=id,
        )
    )


async def user_data_stream_subscribe_signature(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Subscribe to User Data Stream through signature subscription
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.user_data_stream_subscribe_signature(
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_user_data_stream_subscribe_signature(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        user_data_stream_subscribe_signature(
            client=client,
            id=id,
        )
    )


async def user_data_stream_stop(
        client: Spot,
        listen_key: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Explicitly stop and close the user data stream.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.user_data_stream_stop(
            listen_key=listen_key,
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_user_data_stream_stop(
        client: Spot,
        listen_key: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        user_data_stream_stop(
            client=client,
            listen_key=listen_key,
            id=id,
        )
    )


async def user_data_stream_start(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Start a new user data stream.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.user_data_stream_start(
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_user_data_stream_start(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        user_data_stream_start(
            client=client,
            id=id,
        )
    )


async def user_data_stream_ping(
        client: Spot,
        listen_key: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Start a new user data stream.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.user_data_stream_ping(
            listen_key=listen_key,
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_user_data_stream_ping(
        listen_key: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        user_data_stream_ping(
            listen_key=listen_key,
            id=id,
        )
    )
    

async def session_subscriptions(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Listing all subscriptions
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.session_subscriptions(
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_session_subscriptions(
        id: Optional[str] = None,
    ):
    asyncio.run(
        session_subscriptions(
            id=id,
        )
    )