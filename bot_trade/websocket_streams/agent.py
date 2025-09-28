
import asyncio
from binance_sdk_spot.spot import Spot

async def agg_trade(
        client: Spot, 
        symbol: str
        ):
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()

        stream = await connection.agg_trade(symbol=symbol)
        stream.on("message", lambda data: print(f"{data}"))
        await asyncio.sleep(5)
        await stream.unsubscribe()

    except Exception as e:
        print(f"exchange_info() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

def call_agg_trade(
        client: Spot, 
        symbol: str,
        ):
    asyncio.run(agg_trade(client, symbol))