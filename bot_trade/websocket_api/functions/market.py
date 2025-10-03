
import asyncio

from typing import Optional, Union, List

from bot_trade.others.functions import get_data

from collections import defaultdict

from binance_sdk_spot.spot import Spot

from binance_sdk_spot.rest_api.models import KlinesIntervalEnum, Ticker24hrTypeEnum,\
      TickerTypeEnum, TickerWindowSizeEnum, TickerTradingDayTypeEnum, UiKlinesIntervalEnum


async def avg_price(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Get current average price for a symbol.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.avg_price(
            symbol=symbol,
            id=id,
            )
        return get_data(response)
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


async def depth(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ) -> defaultdict:
    """
    Description:
        Get current order book.
        Note that this request returns limited market depth.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.depth(
            symbol=symbol,
            id=id,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_depth(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
    ):
    asyncio.run(
        depth(
            client=client,
            symbol=symbol,
            id=id,
        )
    )


async def klines(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[KlinesIntervalEnum, None],
        id: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        time_zone: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get klines (candlestick bars).
        Klines are uniquely identified by their open & close time.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.klines(
            symbol=symbol,
            interval=interval,
            id=id,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_klines(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[KlinesIntervalEnum, None],
        id: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        time_zone: Optional[str] = None,
        limit: Optional[int] = None,
    ):
    asyncio.run(
        klines(
            client=client,
            symbol=symbol,
            interval=interval,
            id=id,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit
        )
    )


async def ticker_book(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
    ) -> defaultdict:
    """
    Description:
        Get the current best price and quantity on the order book.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ticker_book(
            symbol=symbol,
            id=id,
            symbols=symbols
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ticker_book(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
    ):
    asyncio.run(
        ticker_book(
            client=client,
            symbol=symbol,
            id=id,
            symbols=symbols
        )
    )


async def ticker_price(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
    ) -> defaultdict:
    """
    Description:
        Get the current best price and quantity on the order book.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ticker_price(
            symbol=symbol,
            id=id,
            symbols=symbols
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ticker_price(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
    ):
    asyncio.run(
        ticker_price(
            client=client,
            symbol=symbol,
            id=id,
            symbols=symbols
        )
    )


async def ticker24hr(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        type: Optional[Ticker24hrTypeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Get 24-hour rolling window price change statistics.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ticker24hr(
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ticker24hr(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        type: Optional[Ticker24hrTypeEnum] = None,
    ):
    asyncio.run(
        ticker24hr(
            client=client,
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type
        )
    )


async def ticker(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        type: Optional[TickerTypeEnum] = None,
        window_size: Optional[TickerWindowSizeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Get rolling window price change statistics with a custom window.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ticker(
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type,
            window_size=window_size
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ticker(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        type: Optional[TickerTypeEnum] = None,
        window_size: Optional[TickerWindowSizeEnum] = None,
    ):
    asyncio.run(
        ticker(
            client=client,
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type,
            window_size=window_size
        )
    )


async def ticker_trading_day(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        time_zone: Optional[str] = None,
        type: Optional[TickerTradingDayTypeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Price change statistics for a trading day.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ticker_trading_day(
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type,
            time_zone=time_zone
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ticker_trading_day(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        time_zone: Optional[str] = None,
        type: Optional[TickerTradingDayTypeEnum] = None,
    ):
    asyncio.run(
        ticker_trading_day(
            client=client,
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type,
            time_zone=time_zone
        )
    )


async def trades_aggregate(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        time_zone: Optional[str] = None,
        type: Optional[TickerTradingDayTypeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Price change statistics for a trading day.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.trades_aggregate(
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type,
            time_zone=time_zone
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_trades_aggregate(
        client: Spot,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        time_zone: Optional[str] = None,
        type: Optional[TickerTradingDayTypeEnum] = None,
    ):
    asyncio.run(
        trades_aggregate(
            client=client,
            symbol=symbol,
            id=id,
            symbols=symbols,
            type=type,
            time_zone=time_zone
        )
    )


async def trades_historical(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        from_id: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get historical trades.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.trades_historical(
            symbol=symbol,
            id=id,
            from_id=from_id,
            limit=limit
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_trades_historical(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        from_id: Optional[int] = None,
        limit: Optional[int] = None,
    ):
    asyncio.run(
        trades_historical(
            client=client,
            symbol=symbol,
            id=id,
            from_id=from_id,
            limit=limit
        )
    )


async def trades_recent(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get recent trades.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.trades_recent(
            symbol=symbol,
            id=id,
            limit=limit
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_trades_recent(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        limit: Optional[int] = None,
    ):
    asyncio.run(
        trades_recent(
            client=client,
            symbol=symbol,
            id=id,
            limit=limit
        )
    )


async def ui_klines(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[UiKlinesIntervalEnum, None],
        id: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        time_zone: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get klines (candlestick bars) optimized for presentation.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.ui_klines(
            symbol=symbol,
            interval=interval,
            id=id,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_ui_klines(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[UiKlinesIntervalEnum, None],
        id: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        time_zone: Optional[str] = None,
        limit: Optional[int] = None,
    ):
    asyncio.run(
        ui_klines(
            client=client,
            symbol=symbol,
            interval=interval,
            id=id,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit
        )
    )