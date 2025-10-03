
import asyncio

from typing import Union
from typing import Optional

from bot_trade.others.functions import get_data

from collections import defaultdict

from binance_sdk_spot.spot import Spot


async def account_comission(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Get current account commission rates.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.account_commission(
            symbol=symbol, 
            id=id)
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_account_comission(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(account_comission(
        client=client,
        symbol=symbol,
        id=id))


async def all_orders(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query information about all your orders - active, canceled, filled - 
        filtered by time range.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.all_orders(
            symbol = symbol,
            id = id,
            order_id = order_id,
            start_time = start_time,
            end_time = end_time,
            limit = limit,
            recv_window = recv_window,
        )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_all_orders(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(all_orders(
        client=client,
            symbol = symbol,
            id = id,
            order_id = order_id,
            start_time = start_time,
            end_time = end_time,
            limit = limit,
            recv_window = recv_window,))


async def all_order_lists(
        client: Spot,
        id: Optional[str] = None,
        from_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query information about all your order lists, filtered by time range.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.all_order_lists(
            id=id,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window
        )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_all_order_lists(
        client: Spot,
        id: Optional[str] = None,
        from_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(all_order_lists(
        client=client,
        id=id,
        from_id=from_id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        recv_window=recv_window))


async def account_status(
        client: Spot,
        id: Optional[str] = None,
        omit_zero_balances: Optional[bool] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query information about your account.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.account_status(
            id=id,
            omit_zero_balances=omit_zero_balances,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_account_status(
        client: Spot,
        id: Optional[str] = None,
        omit_zero_balances: Optional[bool] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(account_status(
        client=client,
        id=id,
        omit_zero_balances=omit_zero_balances,
        recv_window=recv_window))


async def account_rate_limits_orders(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.account_rate_limits_orders(
            id=id,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_account_rate_limits_orders(
        client: Spot,
        id: Optional[str] = None,
        omit_zero_balances: Optional[bool] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(account_rate_limits_orders(
        client=client,
        id=id,
        omit_zero_balances=omit_zero_balances,
        recv_window=recv_window))


async def my_allocations(
        client: Spot,
        
    ) -> defaultdict:
    """
    Description:
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.my_allocations(
            
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_my_allocations(
        client: Spot,
        
    ):
    asyncio.run(my_allocations(
        client=client,
        
        ))

