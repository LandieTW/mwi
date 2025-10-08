

import msvcrt
import asyncio
import logging
from rest_api.functions import rest_api_market 


'N° decimal places'
decimal = 2


class KlineAnalysis:
    '''
    Extract kline result
    '''


    def __init__(self, client):
        self.client = client
        self.kline_data = {}
        self.shutdown_event = asyncio.Event()
        self.graph_stats = {}


    async def shutdown(self):
        """
        Description:
            Verify if 'Esc' is pressed, than shutdown get_kline
        """
        while True:
            if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':
                self.shutdown_event.set()
                break
            await asyncio.sleep(0.1)


    async def get_kline(self):
        """
        Description:
            Get graph data in real time
        """
        def message_handler(data):
            """
            Description:
                Save retrieved kline data
            """
            if not self.shutdown_event.is_set():
                self.kline_data = {
                        "Open time": int(data.k.t),
                        "Close time": int(data.k.T),
                        "Symbol": str(data.k.s),
                        "Interval": str(data.k.i),
                        "First trade ID": int(data.k.f),
                        "Last trade ID": int(data.k.L),
                        "Open price": round(float(data.k.o), decimal),
                        "Close price": round(float(data.k.c), decimal),
                        "High price": round(float(data.k.h), decimal),
                        "Low price": round(float(data.k.l), decimal),
                        "Base asset volume": round(float(data.k.v), decimal),
                        "Number of trades": int(data.k.n),
                        "Is kline close": bool(data.k.x),
                        "Quote asset volume": round(float(data.k.q), decimal),
                        "Taker buy base volume": round(float(data.k.V), decimal),
                        "Taker buy quote volume": round(float(data.k.Q), decimal),
                        "Ignore": str(data.k.B)
                }
                print(f"Klines:\n {self.kline_data}")

        connection = None
        try:
            connection = await self.client.websocket_streams.create_connection()
            stream = await connection.kline(symbol="BTCUSDT", interval='1s')
            stream.on("message", message_handler)
            
            await self.shutdown_event.wait()
            await stream.unsubscribe()

        except Exception as e:
            logging.error(f"kline() error: {e}")
        finally:
            if connection:
                await connection.close_connection(close_session=True)
    

    async def statistics(self):
        """
        Description:
            Gets last 24h graph statistics
        """
        while not self.shutdown_event.is_set():
            ticker = rest_api_market.ticker(
                client=self.client,
                symbol="BTCUSDT"
            )['data'].actual_instance

            self.graph_stats = {
                "Symbol": str(ticker.symbol),
                "Price_change": round(float(ticker.price_change), decimal),
                "Price_change_percent": round(float(ticker.price_change_percent), decimal),
                "Weighted_avg_price": round(float(ticker.weighted_avg_price), decimal),
                "Open_price": round(float(ticker.open_price), decimal),
                "High_price": round(float(ticker.high_price), decimal),
                "Low_price": round(float(ticker.low_price), decimal),
                "Last_price": round(float(ticker.last_price), decimal),
                "Volume": round(float(ticker.volume), decimal),
                "Quote_volume": round(float(ticker.quote_volume), decimal),
                "Open_time": int(ticker.open_time),
                "Close_time": int(ticker.close_time),
                "First_id": int(ticker.first_id),
                "Last_id": int(ticker.last_id),
                "Count": int(ticker.count)
            }

            print(f"Ticker \n {self.graph_stats}")
            await asyncio.sleep(5)


    async def gather_routines(self):
        '''
        Gather various tasks routines and execute it as in parallel proccess
        '''
        await asyncio.gather(
            self.get_kline(),
            self.shutdown(),
            self.statistics(),
            return_exceptions=True
        )
