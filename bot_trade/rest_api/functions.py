
from typing import Union
from typing import Optional

from collections import defaultdict

from binance_sdk_spot.spot import Spot
from binance_common.models import ApiResponse

def get_data(
        response: ApiResponse
    ) -> defaultdict:
    """
    Description:
        Return response information
    """
    info = defaultdict()
    info['headers'] = response.headers
    info['status'] = response.status
    info['rate_limits'] = response.rate_limits
    info['data'] = response.data()
    return info


def account_comission(
        client: Spot,
        symbol: Union[str, None]
    ) -> defaultdict:
    """
    Description:
        Get current account commission rates.
    """
    return get_data(
        client.rest_api.account_commission(
            symbol=symbol
        )
    )


def all_order_list(
        client: Spot,
        from_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Retrieves all order lists based on provided optional parameters.
    """
    return get_data(
        client.rest_api.all_order_list(
            from_id = from_id,
            start_time = start_time,
            end_time = end_time, limit = limit, recv_window = recv_window,
        )
    )


def all_orders(
        client: Spot,
        symbol: Union[str, None],
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get all account orders; active, canceled, or filled.
    """
    return get_data(
        client.rest_api.all_orders(
            symbol = symbol,
            order_id = order_id,
            start_time = start_time,
            end_time = end_time,
            limit = limit,
            recv_window = recv_window
        )
    )


def get_account(
        client: Spot,
        omit_zero_balances: Optional[bool] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get current account information.
    """
    return get_data(
        client.rest_api.get_account(
            omit_zero_balances = omit_zero_balances,
            recv_window = recv_window,
        )
    )


def get_open_orders(
        client: Spot,
        symbol: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get all open orders on a symbol. 
        **Careful** when accessing this with no symbol.
    """
    return get_data(
        client.rest_api.get_open_orders(
            symbol = symbol,
            recv_window = recv_window
        )
    )


def get_order_list(
        client: Spot,
        order_list_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Retrieves a specific order list based on provided optional parameters.
    """
    return get_data(
        client.rest_api.get_order_list(
            order_list_id= order_list_id,
            orig_client_order_id= orig_client_order_id,
            recv_window= recv_window
        )
    )


def get_order(
        client: Spot,
        symbol: Union[str, None],
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Check an order's status.
    """
    return get_data(
        client.rest_api.get_order(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window
        )
    )


def my_allocations(
        client: Spot,
        symbol: Union[str, None],
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
    return get_data(
        client.rest_api.my_allocations(
            symbol=symbol,
            start_time=start_time,
            end_time=end_time,
            from_allocation_id=from_allocation_id,
            limit=limit,
            order_id=order_id,
            recv_window=recv_window
        )
    )


def my_prevented_matches(
        client: Spot,
        symbol: Union[str, None],
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
    return get_data(
        client.rest_api.my_prevented_matches(
            symbol=symbol,
            prevented_match_id=prevented_match_id,
            order_id=order_id,
            from_prevented_match_id=from_prevented_match_id,
            limit=limit,
            recv_window=recv_window
        )
    )


def my_trades(
        client: Spot,
        symbol: Union[str, None],
        order_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        from_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get trades for a specific account and symbol.
    """
    return get_data(
        client.rest_api.my_trades(
            symbol=symbol,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window
        )
    )


def open_order_list(
        client: Spot,
        recv_window: Optional[int] = None
    ) -> defaultdict:
    """
    Description:
        Query Open Order lists
    """
    return get_data(
        client.rest_api.open_order_list(
            recv_window=recv_window
        )
    )


def order_ammendments(
        client: Spot,
        symbol: Union[str, None],
        order_id: Union[int, None],
        from_execution_id: Optional[int] = None,
        limit: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Descritpion:
        Queries all amendments of a single order.
    """
    return get_data(
        client.rest_api.order_amendments(
            symbol=symbol,
            order_id=order_id,
            from_execution_id=from_execution_id,
            limit=limit,
            recv_window=recv_window
        )
    )


def rate_limit_order(
        client: Spot,
        recv_window: Optional[int] = None
    ) -> defaultdict:
    """
    Description:
        Displays the user's unfilled order count for all intervals.
    """
    return get_data(
        client.rest_api.rate_limit_order(
            recv_window=recv_window
        )
    )
