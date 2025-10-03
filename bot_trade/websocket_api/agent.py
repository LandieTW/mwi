
from typing import Optional, List
from collections import defaultdict
from bot_trade.others.functions import get_data
import asyncio
from binance_sdk_spot.websocket_api.models import ExchangeInfoSymbolStatusEnum
from binance_sdk_spot.spot import Spot

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

        response = await client.websocket_api.exchange_info(
            id=id,
            symbol=symbol,
            symbols=symbols,
            permissions=permissions,
            show_permission_sets=show_permission_sets,
            symbol_status=symbol_status
        )

        return get_data(response)
    
    except Exception as e:
        print(f"exchange_info() error: {e}")
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
    asyncio.run(exchange_info(
            client,
            id=id,
            symbol=symbol,
            symbols=symbols,
            permissions=permissions,
            show_permission_sets=show_permission_sets,
            symbol_status=symbol_status))
