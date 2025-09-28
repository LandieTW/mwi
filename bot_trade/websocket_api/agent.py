
import asyncio
from binance_sdk_spot.websocket_api.models import exchange_info_response_result
from binance_sdk_spot.spot import Spot

async def exchange_info(
        client: Spot, 
        symbol: str,
        ):
    connection = None
    try:
        connection = await client.websocket_api.create_connection()

        response = await client.websocket_api.exchange_info(symbol=symbol)

        rate_limits = response.rate_limits
        for rate in rate_limits:
            print("Rate Limits: ", rate)

        data: exchange_info_response_result = response.data()
        print(f"exchange_info() response: {data}")
    except Exception as e:
        print(f"exchange_info() error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)

def call_exchange_info(
        client: Spot, 
        symbol: str
        ):
    asyncio.run(exchange_info(client, symbol))
