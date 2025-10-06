
import asyncio
from typing import Optional, Union
from others.other_functions import get_data
from collections import defaultdict
from binance_sdk_spot.spot import Spot
from binance_sdk_spot.websocket_streams.models import (AllMarketRollingWindowTickerWindowSizeEnum,\
    RollingWindowTickerWindowSizeEnum, PartialBookDepthLevelsEnum, KlineIntervalEnum)


async def avg_price(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Average price streams push changes in the average price over a fixed time interval.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.avg_price(
            symbol=symbol,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_avg_price(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        avg_price(
            client=client,
            symbol=symbol,
            id=id,
        )
    )


async def all_ticker(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket All Market Tickers Stream
        24hr rolling window ticker statistics for all symbols that changed in an array. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the 
        previous 24hrs. Note that only tickers that have changed will be present in the array.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.all_ticker(
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_all_ticker(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        all_ticker(
            client=client,
            id=id,
        )
    )


async def all_mini_ticker(
        client: Spot,
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket All Market Mini Tickers Stream
        24hr rolling window mini-ticker statistics for all symbols that changed in an array. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the 
        previous 24hrs. Note that only tickers that have changed will be present in the array.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.all_mini_ticker(
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_all_mini_ticker(
        client: Spot,
        id: Optional[str] = None,
    ):
    asyncio.run(
        all_mini_ticker(
            client=client,
            id=id,
        )
    )


async def all_market_rolling_window_ticker(
        client: Spot,
        window_size: Union[AllMarketRollingWindowTickerWindowSizeEnum, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket All Market Mini Tickers Stream
        24hr rolling window mini-ticker statistics for all symbols that changed in an array. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the 
        previous 24hrs. Note that only tickers that have changed will be present in the array.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.all_market_rolling_window_ticker(
            window_size=window_size,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_all_market_rolling_window_ticker(
        client: Spot,
        window_size: Union[AllMarketRollingWindowTickerWindowSizeEnum, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        all_market_rolling_window_ticker(
            client=client,
            window_size=window_size,
            id=id,
        )
    )
    

async def agg_trade(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
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
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_agg_trade(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        agg_trade(
            client=client,
            symbol=symbol,
            id=id,
        )
    )


async def trade(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Trade Streams
        The Trade Streams push raw trade information; each trade has a unique buyer and seller.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.trade(
            symbol=symbol,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_trade(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        trade(
            client=client,
            symbol=symbol,
            id=id,
        )
    )


async def ticker(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Individual Symbol Ticker Streams
        24hr rolling window ticker statistics for a single symbol. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the 
        previous 24hrs.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.ticker(
            symbol=symbol,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ticker(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        ticker(
            client=client,
            symbol=symbol,
            id=id,
        )
    )


async def rolling_window_ticker(
        client: Spot,
        symbol: Union[str, None],
        window_size: Union[RollingWindowTickerWindowSizeEnum, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Individual Symbol Ticker Streams
        24hr rolling window ticker statistics for a single symbol. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the 
        previous 24hrs.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.rolling_window_ticker(
            symbol=symbol,
            window_size=window_size,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_rolling_window_ticker(
        client: Spot,
        symbol: Union[str, None],
        window_size: Union[RollingWindowTickerWindowSizeEnum, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        rolling_window_ticker(
            client=client,
            symbol=symbol,
            window_size=window_size,
            id=id,
        )
    )


async def partial_book_depth(
        client: Spot,
        symbol: Union[str, None],
        levels: Union[PartialBookDepthLevelsEnum, None],
        id: Optional[str] = None,
        update_speed: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Partial Book Depth Streams
        Top **levels** bids and asks, pushed every second. 
        Valid **levels** are 5, 10, or 20.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.partial_book_depth(
            symbol=symbol,
            levels=levels,
            id=id,
            update_speed=update_speed
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_partial_book_depth(
        client: Spot,
        symbol: Union[str, None],
        levels: Union[PartialBookDepthLevelsEnum, None],
        id: Optional[str] = None,
        update_speed: Optional[str] = None,
    ):
    asyncio.run(
        partial_book_depth(
            client=client,
            symbol=symbol,
            levels=levels,
            id=id,
            update_speed=update_speed
        )
    )


async def mini_ticker(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Individual Symbol Mini Ticker Stream
        24hr rolling window mini-ticker statistics. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for 
        the previous 24hrs.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.mini_ticker(
            symbol=symbol,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_mini_ticker(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        mini_ticker(
            client=client,
            symbol=symbol,
            id=id,
        )
    )


async def kline(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[KlineIntervalEnum, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Individual Symbol Mini Ticker Stream
        24hr rolling window mini-ticker statistics. 
        These are NOT the statistics of the UTC day, but a 24hr rolling window for 
        the previous 24hrs.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.kline(
            symbol=symbol,
            interval=interval,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_kline(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[KlineIntervalEnum, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        kline(
            client=client,
            symbol=symbol,
            interval=interval,
            id=id,
        )
    )


async def kline_offset(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[KlineIntervalEnum, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Kline/Candlestick Streams with timezone offset
        The Kline/Candlestick Stream push updates to the current klines/candlestick 
        every second in `UTC+8` timezone
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.kline_offset(
            symbol=symbol,
            interval=interval,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_kline_offset(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[KlineIntervalEnum, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        kline_offset(
            client=client,
            symbol=symbol,
            interval=interval,
            id=id,
        )
    )


async def diff_book_depth(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        update_speed: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Diff. Depth Stream
        Order book price and quantity depth updates used to locally manage an order book.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.diff_book_depth(
            symbol=symbol,
            id=id,
            update_speed=update_speed
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_diff_book_depth(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        update_speed: Optional[str] = None,
    ):
    asyncio.run(
        diff_book_depth(
            client=client,
            symbol=symbol,
            id=id,
            update_speed=update_speed
        )
    )


async def book_ticker(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        WebSocket Individual Symbol Book Ticker Streams
        Pushes any update to the best bid or ask's price or quantity in real-time 
        for a specified symbol.
    """
    connection = None
    try:
        connection = await client.websocket_streams.create_connection()
        stream = await connection.book_ticker(
            symbol=symbol,
            id=id,
            )
        return get_data(stream)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_book_ticker(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        book_ticker(
            client=client,
            symbol=symbol,
            id=id,
        )
    )
