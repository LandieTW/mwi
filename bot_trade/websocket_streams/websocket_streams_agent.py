
from typing import Optional
import asyncio
from binance_sdk_spot.spot import Spot
from others.other_functions import get_data

async def agg_trade(
        client: Spot, 
        symbol: str,
        id: Optional[str] = None,
        ):
    """
    Description:
        WebSocket Aggregate Trade Streams
        The Aggregate Trade Streams push trade information that is aggregated for a 
        single taker order.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.agg_trade(
            symbol=symbol,
            id=id
            )
        return get_data(stream)

    except Exception as e:
        print(f"exchange_info() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

def call_agg_trade(
        client: Spot, 
        symbol: str,
        id: Optional[str] = None,
        ):
    asyncio.run(agg_trade(
        client=client, 
        symbol=symbol,
        id=id
        ))