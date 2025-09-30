
from typing import List
from typing import Union
from typing import Optional

from collections import defaultdict

from binance_sdk_spot.spot import Spot
from binance_common.models import ApiResponse
from binance_sdk_spot.rest_api.models import TickerTradingDayTypeEnum
from binance_sdk_spot.rest_api.models import TickerWindowSizeEnum
from binance_sdk_spot.rest_api.models import TickerTypeEnum
from binance_sdk_spot.rest_api.models import UiKlinesIntervalEnum
from binance_sdk_spot.rest_api.models import Ticker24hrTypeEnum


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


def agg_trades(
        client: Spot,
        symbol: Union[str, None],
        from_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get compressed, aggregate trades. Trades that fill at the time, 
        from the same taker order, with the same price will have the quantity aggregated.
    """
    return get_data(
        client.rest_api.agg_trades(
            symbol=symbol,
            from_id=from_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
    )


def avg_price(
        client: Spot,
        symbol: Union[str, None],
    ) -> defaultdict:
    """
    Description:
        Current average price for a symbol.
    """
    return get_data(
        client.rest_api.avg_price(
            symbol=symbol,
        )
    )


def depth(
        client: Spot,
        symbol: Union[str, None],
        limit: Optional[int] = None
    ) -> defaultdict:
    """
    Description:
        Order book
    """
    return get_data(
        client.rest_api.depth(
            symbol=symbol,
            limit=limit
        )
    )


def ticker_book_ticker(
        client: Spot,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
    ) -> defaultdict:
    """
    Description:
        Best price/qty on the order book for a symbol or symbols.
    """
    return get_data(
        client.rest_api.ticker_book_ticker(
            symbol=symbol,
            symbols=symbols,
        )
    )


def historical_trades(
        client: Spot,
        symbol: Union[str, None],
        limit: Optional[int] = None,
        from_id: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get older market trades.
    """
    return get_data(
        client.rest_api.historical_trades(
            symbol=symbol,
            limit=limit,
            from_id=from_id,
        )
    )


def ticker_price(
        client: Spot,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
    ) -> defaultdict:
    """
    Description:
        Latest price for a symbol or symbols.
    """
    return get_data(
        client.rest_api.ticker_price(
            symbol=symbol,
            symbols=symbols,
        )
    )


def get_trades(
        client: Spot,
        symbol: Union[str, None],
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get recent market trades.
    """
    return get_data(
        client.rest_api.get_trades(
            symbol=symbol,
            limit=limit,
        )
    )


def klines(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[str, None],
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        time_zone: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Kline/candlestick bars for a symbol. 
        Klines are uniquely identified by their open time.
    """
    return get_data(
        client.rest_api.klines(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit,
        )
    )


def ticker_trading_day(
        client: Spot,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        time_zone: Optional[str] = None,
        type: Optional[TickerTradingDayTypeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Price change statistics for a trading day.
    """
    return get_data(
        client.rest_api.ticker_trading_day(
            symbol=symbol,
            symbols=symbols,
            time_zone=time_zone,
            type=type,
        )
    )


def ui_klines(
        client: Spot,
        symbol: Union[str, None],
        interval: Union[UiKlinesIntervalEnum, None],
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        time_zone: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Kline/candlestick bars for a symbol. 
        Klines are uniquely identified by their open time.
    """
    return get_data(
        client.rest_api.ui_klines(
            symbol=symbol,
            interval=interval,
            start_time=start_time,
            end_time=end_time,
            time_zone=time_zone,
            limit=limit,
        )
    )


def ticker(
        client: Spot,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        window_size: Optional[TickerWindowSizeEnum] = None,
        type: Optional[TickerTypeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        24 hour price change statistics for a symbol or symbols.
    """
    return get_data(
        client.rest_api.ticker(
            symbol=symbol,
            symbols=symbols,
            window_size=window_size,
            type=type,
        )
    )


def ticker24hr(
        client: Spot,
        symbol: Optional[str] = None,
        symbols: Optional[List[str]] = None,
        type: Optional[Ticker24hrTypeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        24 hour rolling window price change statistics. 
        **Careful** when accessing this with no symbol.
    """
    return get_data(
        client.rest_api.ticker24hr(
            symbol=symbol,
            symbols=symbols,
            type=type,
        )
    )

