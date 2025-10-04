
import asyncio
from typing import Union, Optional
from others.other_functions import get_data
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
        Query your current unfilled order count for all intervals.
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
        symbol: Union[str, None],
        id: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        from_allocation_id: Optional[int] = None,
        limit: Optional[int] = None,
        order_id: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Retrieves allocations resulting from SOR order placement.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.my_allocations(
            symbol=symbol,
            id=id,
            start_time=start_time,
            end_time=end_time,
            from_allocation_id=from_allocation_id,
            limit=limit,
            order_id=order_id,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_my_allocations(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        from_allocation_id: Optional[int] = None,
        limit: Optional[int] = None,
        order_id: Optional[int] = None,
        recv_window: Optional[int] = None,        
    ):
    asyncio.run(my_allocations(
        client=client,
        symbol=symbol,
        id=id,
        start_time=start_time,
        end_time=end_time,
        from_allocation_id=from_allocation_id,
        limit=limit,
        order_id=order_id,
        recv_window=recv_window        
        ))


async def my_prevented_matches(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        prevented_match_id: Optional[int] = None,
        order_id: Optional[int] = None,
        from_prevented_match_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Displays the list of orders that were expired due to STP.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.my_prevented_matches(
            symbol=symbol,
            id=id,
            prevented_match_id=prevented_match_id,
            order_id=order_id,
            from_prevented_match_id=from_prevented_match_id,
            limit=limit,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_my_prevented_matches(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        prevented_match_id: Optional[int] = None,
        order_id: Optional[int] = None,
        from_prevented_match_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,    
    ):
    asyncio.run(my_prevented_matches(
            client=client,
            symbol=symbol,
            id=id,
            prevented_match_id=prevented_match_id,
            order_id=order_id,
            from_prevented_match_id=from_prevented_match_id,
            limit=limit,
            recv_window=recv_window       
        ))
    

async def my_trades(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        from_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query information about all your trades, filtered by time range.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.my_trades(
            symbol=symbol,
            id=id,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_my_trades(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        from_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,  
    ):
    asyncio.run(my_trades(
            client=client,
            symbol=symbol,
            id=id,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window      
        ))


async def open_order_lists_status(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query execution status of all open order lists.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.open_order_lists_status(
            id=id,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_open_order_lists_status(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(open_order_lists_status(
            client=client,
            id=id,
            recv_window=recv_window     
        ))


async def open_order_lists_status(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query execution status of all open order lists.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.open_order_lists_status(
            id=id,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_open_order_lists_status(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(open_order_lists_status(
            client=client,
            id=id,
            recv_window=recv_window     
        ))


async def open_orders_status(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Query execution status of all open order lists.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.open_orders_status(
            id=id,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_open_orders_status(
        client: Spot,
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(open_orders_status(
            client=client,
            id=id,
            recv_window=recv_window     
        ))


async def order_amendments(
        client: Spot,
        symbol: Union[str, None],
        order_id: Union[int, None],
        id: Optional[str] = None,
        from_execution_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Queries all amendments of a single order.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_amendments(
            symbol=symbol,
            order_id=order_id,
            id=id,
            from_execution_id=from_execution_id,
            limit=limit,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_amendments(
        client: Spot,
        symbol: Union[str, None],
        order_id: Union[int, None],
        id: Optional[str] = None,
        from_execution_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(order_amendments(
            client=client,
            symbol=symbol,
            order_id=order_id,
            id=id,
            from_execution_id=from_execution_id,
            limit=limit,
            recv_window=recv_window     
        ))


async def order_list_status(
        client: Spot,
        symbol: Union[str, None],
        order_id: Union[int, None],
        id: Optional[str] = None,
        from_execution_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Queries all amendments of a single order.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_list_status(
            symbol=symbol,
            order_id=order_id,
            id=id,
            from_execution_id=from_execution_id,
            limit=limit,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_list_status(
        client: Spot,
        symbol: Union[str, None],
        order_id: Union[int, None],
        id: Optional[str] = None,
        from_execution_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(order_list_status(
            client=client,
            symbol=symbol,
            order_id=order_id,
            id=id,
            from_execution_id=from_execution_id,
            limit=limit,
            recv_window=recv_window     
        ))


async def order_status(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Check execution status of an order.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_status(
            symbol=symbol,
            order_id=order_id,
            id=id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window
        )   
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_status(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(order_status(
            client=client,
            symbol=symbol,
            order_id=order_id,
            id=id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window     
        ))
