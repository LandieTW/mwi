
from typing import List
from typing import Optional

from bot_trade.others.functions import get_data
from collections import defaultdict

from binance_sdk_spot.spot import Spot
from binance_sdk_spot.rest_api.models import ExchangeInfoSymbolStatusEnum


def exchange_info(
        client: Spot,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        permissions: Optional[List[str]] = None,
        show_permission_sets: Optional[bool] = None,
        symbol_status: Optional[ExchangeInfoSymbolStatusEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Current exchange trading rules and symbol information
    """
    return get_data(
        client.rest_api.exchange_info(
            symbol=symbol,
            symbols=symbols,
            permissions=permissions,
            show_permission_sets=show_permission_sets,
            symbol_status=symbol_status
        )
    )


def ping(
        client: Spot,
    ) -> defaultdict:
    """
    Description:
        Test connectivity to the Rest API.
    """
    return get_data(
        client.rest_api.ping()
    )


def time(
        client: Spot,
    ) -> defaultdict:
    """
    Description
        Test connectivity to the Rest API and get the current server time.
    """
    return get_data(
        client.rest_api.time()
    )
