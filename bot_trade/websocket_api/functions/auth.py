
import asyncio
from typing import Optional
from others.other_functions import get_data
from collections import defaultdict
from binance_sdk_spot.spot import Spot


async def session_status(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Query the status of the WebSocket connection,
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.session_status(
            id=id
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_session_status(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        session_status(
            client=client,
            id=id
        )
    )


async def session_logout(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Forget the API key previously authenticated.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.session_logout(
            id=id
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_session_logout(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        session_logout(
            client=client,
            id=id
        )
    )


async def session_logon(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Authenticate WebSocket connection using the provided API key.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.session_logon(
            id=id,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_session_logon(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        session_logon(
            client=client,
            id=id,
            recv_window=recv_window
        )
    )