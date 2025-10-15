
import os
import indicators
import msvcrt
import asyncio
import logging
import pandas as pd
from collections import deque


'N° decimal places'
decimal = 2
this_path = os.path.dirname(__file__)


class KlineAnalysis:
    '''
    Extract kline result
    '''

    def __init__(self, client):
        self.client = client
        self.df_size = 100
        self.export_data = pd.DataFrame()
        self.buffer_size = 5
        self.kline_data = deque(maxlen=self.buffer_size)
        self.shutdown_event = asyncio.Event()
        self.symbol = "BTCUSDT"
        self.interval = '1m'
        self.order = False      # If True, order will be sent to the exchange
        

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

                '''
                candle = {
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
                '''
                
                candle = {
                    "open": round(float(data.k.o), decimal),
                    "close": round(float(data.k.c), decimal),
                    "high": round(float(data.k.h), decimal),
                    "low": round(float(data.k.l), decimal),
                    "volume": round(float(data.k.v), decimal),
                }
                self.kline_data.append(candle)
                print(self.export_data.tail(50))

                if len(self.kline_data) >= self.buffer_size:
                    df_new = pd.DataFrame(self.kline_data)
                    self.export_data = pd.concat([self.export_data, df_new], ignore_index=True)
                    self.export_data = indicators.ikh(self.export_data)
                    if len(self.export_data) >= self.df_size:
                        self.export_data = self.export_data.iloc[-self.df_size:].reset_index(drop=True)
                    self.kline_data.clear()


        connection = None
        try:
            connection = await self.client.websocket_streams.create_connection()
            stream = await connection.kline(symbol=self.symbol, interval=self.interval)
            stream.on("message", message_handler)
            
            await self.shutdown_event.wait()
            await stream.unsubscribe()

        except Exception as e:
            logging.error(f"kline() error: {e}")
        finally:
            if connection:
                await connection.close_connection(close_session=True)
    

    async def gather_routines(self):
        '''
        Gather various tasks routines and execute it as in parallel proccess
        '''
        await asyncio.gather(
            self.get_kline(),
            self.shutdown(),
            return_exceptions=True
        )
