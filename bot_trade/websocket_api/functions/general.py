
import asyncio

from typing import Optional
from typing import List

from bot_trade.others.functions import get_data

from collections import defaultdict

from binance_sdk_spot.spot import Spot

from binance_sdk_spot.rest_api.models import ExchangeInfoSymbolStatusEnum


async def time(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Test connectivity to the WebSocket API and get the current server time.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.time(
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_time(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        time(
            client=client,
            id=id,
        )
    )


async def ping(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Test connectivity to the WebSocket API.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ping(
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ping(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        ping(
            client=client,
            id=id,
        )
    )


async def exchange_info(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        permissions: Optional[List[str]] = None,
        show_permission_sets: Optional[bool] = None,
        symbol_status: Optional[ExchangeInfoSymbolStatusEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Query current exchange trading rules, rate limits, and symbol information.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.exchange_info(
            id=id,
            symbol=symbol,
            symbols=symbols,
            permissions=permissions,
            show_permission_sets=show_permission_sets,
            symbol_status=symbol_status
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_exchange_info(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        permissions: Optional[List[str]] = None,
        show_permission_sets: Optional[bool] = None,
        symbol_status: Optional[ExchangeInfoSymbolStatusEnum] = None,
    ):
    asyncio.run(
        exchange_info(
            client=client,
            id=id,
            symbol=symbol,
            symbols=symbols,
            permissions=permissions,
            show_permission_sets=show_permission_sets,
            symbol_status=symbol_status
        )
    )