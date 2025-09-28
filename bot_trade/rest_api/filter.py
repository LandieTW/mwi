"""Module for defining various trading filters for symbols on Binance's API."""

class Filter:
    """
    Description:
        The Filter defines the price rules for a symbol.
            - filterType = defines wichh filter is being used.
            - args = dictionary with the arguments of the filter
    """
    def __init__(
            self,
            filtertype: str,
            args: dict = {},
            ):
        self.filtertype = filtertype
        if filtertype == 'PRICE_FILTER':
            return self.PriceFilter(**args)
        elif filtertype == 'PERCENT_PRICE':
            return self.PercentPriceFilter(**args)
        elif filtertype == 'PERCENT_PRICE_BY_SIDE':
            return self.PercentPricebySideFilter(**args)
        elif filtertype == 'LOT_SIZE':
            return self.LostSizeFilter(**args)
        elif filtertype == 'MIN_NOTIONAL':
            return self.MinNotionalFilter(**args)
        elif filtertype == 'NOTIONAL':
            return self.NotionalFilter(**args)
        elif filtertype == 'ICEBERG_PARTS':
            return self.IceberPartsFilter(**args)
        elif filtertype == 'MARKET_LOT_SIZE':
            return self.MarketLotSizeFilter(**args)
        elif filtertype == 'MAX_NUM_ORDERS':
            return self.MaxNumOrdersFilter(**args)
        elif filtertype == 'MAX_NUM_ALGO_ORDERS':
            return self.MaxNumAlgoOrdersFilter(**args)
        elif filtertype == 'MAX_NUM_ICEBERG_ORDERS':
            return self.MaxNumIcebergOrdersFilter(**args)
        elif filtertype == 'MAX_POSITION':
            return self.MaxPositionFilter(**args)
        elif filtertype == 'TRAILING_DELTA':
            return self.TrailingDeltaFilter(**args)
        elif filtertype == 'MAX_NUM_ORDER_AMENDS':
            return self.MaxNumOrderAmendsFilter(**args)
        elif filtertype == 'MAX_NUM_ORDER_LISTS':
            return self.MaxNumOrderListsFilter(**args)
        elif filtertype == 'EXCHANGE_MAX_NUM_ORDERS':
            return self.ExchangeMaxNumOrdersFilter(**args)
        elif filtertype == 'EXCHANGE_MAX_NUM_ALGO_ORDERS':
            return self.ExchangeMaxNumAlgoOrdersFilter(**args)
        elif filtertype == 'EXCHANGE_MAX_NUM_ICEBERG_ORDERS':
            return self.ExchangeMaxNumIcebergOrdersFilter(**args)
        elif filtertype == 'EXCHANGE_MAX_NUM_ORDER_LISTS':
            return self.ExchangeMaxNumOrderListsFilter(**args)
        else:
            raise ValueError(f"THERE'S NO FILTER {filtertype} ON BINANCE'S API")


    def PriceFilter(
            self,
            min_price: float = None,
            max_price: float = None,
            tick_size: float = None,
            ):
        """
        Description:
            The PRICE_FILTER defines the price rules for a symbol. There are 3 parts:
                - minPrice defines the minimum price/stopPrice allowed; disabled on minPrice == 0.
                - maxPrice defines the maximum price/stopPrice allowed; disabled on maxPrice == 0.
                - tickSize defines the intervals that a price/stopPrice can be increased/decreased by; disabled on tickSize == 0.
            Any of the above variables can be set to 0, which disables that rule in the price filter. 
            In order to pass the price filter, the following must be true for price/stopPrice of the enabled rules:
                - price >= minPrice
                - price <= maxPrice
                - price % tickSize == 0
        """
        return {
            "filterType": "PRICE_FILTER",
            "minPrice": str(min_price),
            "maxPrice": str(max_price),
            "tickSize": str(tick_size)
            }


    def PercentPriceFilter(
            self,
            multiplier_up: float = None,
            multiplier_down: float = None,
            avg_price_mins: int = None,
            ):
        """
        Description:
        The PERCENT_PRICE filter defines the valid range for the price based on the average of the previous trades. 
            - avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.
        In order to pass the percent price, the following must be true for price:
            - price <= weightedAveragePrice * multiplierUp
            - price >= weightedAveragePrice * multiplierDown
        """
        return{
            "filterType": "PERCENT_PRICE",
            "multiplierUp": str(multiplier_up),
            "multiplierDown": str(multiplier_down),
            "avgPriceMins": avg_price_mins
            }


    def PercentPricebySideFilter(
            self,
            bid_multiplier_up: float = None,
            bid_multiplier_down: float = None,
            ask_multiplier_up: float = None,
            ask_multiplier_down: float = None,
            avg_price_mins: int = None,
            ):
        """
        Description:
            The PERCENT_PRICE_BY_SIDE filter defines the valid range for the price based on the average of the previous trades.
                - avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.
            There is a different range depending on whether the order is placed on the BUY side or the SELL side.
            Buy orders will succeed on this filter if:
                - Order price <= weightedAveragePrice * bidMultiplierUp
                - Order price >= weightedAveragePrice * bidMultiplierDown
            Sell orders will succeed on this filter if:
                - Order Price <= weightedAveragePrice * askMultiplierUp
                - Order Price >= weightedAveragePrice * askMultiplierDown
        """
        return {
            "filterType": "PERCENT_PRICE_BY_SIDE",
            "bidMultiplierUp": str(bid_multiplier_up),
            "bidMultiplierDown": str(bid_multiplier_down),
            "askMultiplierUp": str(ask_multiplier_up),
            "askMultiplierDown": str(ask_multiplier_down),
            "avgPriceMins": avg_price_mins
        }


    def LostSizeFilter(
            self,
            min_qty: float = None,
            max_qty: float = None,
            step_size: float = None,
    ):
        """
        Description:
            The LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for a symbol. There are 3 parts:
                - minQty defines the minimum quantity/icebergQty allowed.
                - maxQty defines the maximum quantity/icebergQty allowed.
                - stepSize defines the intervals that a quantity/icebergQty can be increased/decreased by.
            In order to pass the lot size, the following must be true for quantity/icebergQty:
                - quantity >= minQty
                - quantity <= maxQty
                - quantity % stepSize == 0
        """
        return {
            "filterType": "LOT_SIZE",
            "minQty": str(min_qty),
            "maxQty": str(max_qty),
            "stepSize": str(step_size)
            }

    
    def MinNotionalFilter(
            self,
            min_notional: float = None,
            apply_to_market: bool = None,
            avg_price_mins: int = None,
    ):
        """
        Description:
            The MIN_NOTIONAL filter defines the minimum notional value allowed for an order on a symbol. 
            An order's notional value is the price * quantity. 
                - applyToMarket determines whether or not the MIN_NOTIONAL filter will also be applied to MARKET orders. 
            Since MARKET orders have no price, the average price is used over the last avgPriceMins minutes. 
                - avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.
        """
        return {
            "filterType": "MIN_NOTIONAL",
            "minNotional": str(min_notional),
            "applyToMarket": apply_to_market,
            "avgPriceMins": avg_price_mins
            }


    def NotionalFilter(
            self,
            min_notional: float = None,
            apply_min_to_market: bool = None,
            max_notional: float = None,
            apply_max_to_market: bool = None,
            avg_price_mins: int = None
    ):
        """
        Description:
            The NOTIONAL filter defines the acceptable notional range allowed for an order on a symbol.
                - applyMinToMarket determines whether the minNotional will be applied to MARKET orders.
                - applyMaxToMarket determines whether the maxNotional will be applied to MARKET orders.
            In order to pass this filter, the notional (price * quantity) has to pass the following conditions:
                - price * quantity <= maxNotional
                - price * quantity >= minNotional
            For MARKET orders, the average price used over the last avgPriceMins minutes will be used for 
            calculation.
            If the avgPriceMins is 0, then the last price will be used.
        """
        return {
            "filterType": "NOTIONAL",
            "minNotional": str(min_notional),
            "applyMinToMarket": apply_min_to_market,
            "maxNotional": str(max_notional),
            "applyMaxToMarket": apply_max_to_market,
            "avgPriceMins": avg_price_mins
            }
    

    def IceberPartsFilter(
            self,
            limit: int = None
    ):
        """
        Description:
            The ICEBERG_PARTS filter defines the maximum parts an iceberg order can have. 
            The number of ICEBERG_PARTS is definesd as CEIL(qty / icebergQty).
        """
        return {
            "filterType": "ICEBERG_PARTS",
            "limit": limit
            }

    
    def MarketLotSizeFilter(
            self,
            min_qty: float = None,
            max_qty: float = None,
            step_size: float = None
    ):
        """
        Description:
            The MARKET_LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for MARKET 
            orders on a symbol. There are 3 parts:
                - minQty defines the minimum quantity allowed.
                - maxQty defines the maximum quantity allowed.
                - stepSize defines the intervals that a quantity can be increased/decreased by.
            In order to pass the market lot size, the following must be true for quantity:
                - quantity >= minQty
                - quantity <= maxQty
                - quantity % stepSize == 0
        """
        return {
            "filterType": "MARKET_LOT_SIZE",
            "minQty": str(min_qty),
            "maxQty": str(max_qty),
            "stepSize": str(step_size)
            }
    

    def MaxNumOrdersFilter(
            self,
            max_num_orders: int = None
    ):
        """
        Description:
            The MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to have open 
            on a symbol. 
            Note that both "algo" orders and normal orders are counted for this filter.
        """
        return {
            "filterType": "MAX_NUM_ORDERS",
            "maxNumOrders": max_num_orders
            }
    
    
    def MaxNumAlgoOrdersFilter(
            self,
            max_num_algo_orders
    ):
        """
        Description:
            The MAX_NUM_ALGO_ORDERS filter defines the maximum number of "algo" orders an account is allowed 
            to have open on a symbol. 
            "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        """
        return {
            "filterType": "MAX_NUM_ALGO_ORDERS",
            "maxNumAlgoOrders": max_num_algo_orders
            }


    def MaxNumIcebergOrdersFilter(
            self,
            max_num_iceber_orders
    ):
        """
        Description:
            The MAX_NUM_ICEBERG_ORDERS filter defines the maximum number of ICEBERG orders an account is allowed 
            to have open on a symbol. 
            An ICEBERG order is any order where the icebergQty is > 0.
        """
        return {
            "filterType": "MAX_NUM_ICEBERG_ORDERS",
            "maxNumIcebergOrders": max_num_iceber_orders
            }


    def MaxPositionFilter(
            self,
            max_position: float = None
    ):
        """
        Description:
            The MAX_POSITION filter defines the allowed maximum position an account can have on the base asset 
            of a symbol. An account's position defined as the sum of the account's:
            free balance of the base asset
            locked balance of the base asset
            sum of the qty of all open BUY orders
            BUY orders will be rejected if the account's position is greater than the maximum position allowed.
            If an order's quantity can cause the position to overflow, this will also fail the MAX_POSITION filter.
        """
        return {
            "filterType":"MAX_POSITION",
            "maxPosition":max_position
            }

    
    def TrailingDeltaFilter(
            self,
            min_trailing_above_delta: int = None,
            max_trailing_above_delta: int = None,
            min_trailing_below_delta: int = None,
            max_trailing_below_delta: int = None
    ):
        """
        Description:
            The TRAILING_DELTA filter defines the minimum and maximum value for the parameter trailingDelta.
            In order for a trailing stop order to pass this filter, the following must be true:
            For STOP_LOSS BUY, STOP_LOSS_LIMIT_BUY,TAKE_PROFIT SELL and TAKE_PROFIT_LIMIT SELL orders:
                - trailingDelta >= minTrailingAboveDelta
                - trailingDelta <= maxTrailingAboveDelta
            For STOP_LOSS SELL, STOP_LOSS_LIMIT SELL, TAKE_PROFIT BUY, and TAKE_PROFIT_LIMIT BUY orders:
                - trailingDelta >= minTrailingBelowDelta
                - trailingDelta <= maxTrailingBelowDelta
        """  
        return {
            "filterType": "TRAILING_DELTA",
            "minTrailingAboveDelta": min_trailing_above_delta,
            "maxTrailingAboveDelta": max_trailing_above_delta,
            "minTrailingBelowDelta": min_trailing_below_delta,
            "maxTrailingBelowDelta": max_trailing_below_delta
        }


    def MaxNumOrderAmendsFilter(
            self,
            max_num_order_amends: int = None
    ):
        """
        Description:
            The MAX_NUM_ORDER_AMENDS filter defines the maximum number of times an order can be amended on 
            the given symbol.
            If there are too many order amendments made on a single order, you will receive the -2038 error code.
        """
        return {
            "filterType": "MAX_NUM_ORDER_AMENDS",
            "maxNumOrderAmends": max_num_order_amends
            }


    def MaxNumOrderListsFilter(
            self,
            max_num_order_lists: int = None
    ):
        """
        Description:
            The MAX_NUM_ORDER_LISTS filter defines the maximum number of open order lists an account can have on a symbol. 
            Note that OTOCOs count as one order list.
        """
        return {
            "filterType": "MAX_NUM_ORDER_LISTS",
            "maxNumOrderLists": max_num_order_lists
            }


    def ExchangeMaxNumOrdersFilter(
            self,
            max_num_orders: int = None
    ):
        """
        Description:
            The EXCHANGE_MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to 
            have open on the exchange. Note that both "algo" orders and normal orders are counted for this filter.
        """
        return {
            "filterType": "EXCHANGE_MAX_NUM_ORDERS",
            "maxNumOrders": max_num_orders
            }

    
    def ExchangeMaxNumAlgoOrdersFilter(
            self,
            max_num_algo_orders: int = None
    ):
        """
        Description:
            The EXCHANGE_MAX_NUM_ALGO_ORDERS filter defines the maximum number of "algo" orders an account is allowed 
            to have open on the exchange. 
            "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        """
        return {
            "filterType": "EXCHANGE_MAX_NUM_ALGO_ORDERS",
            "maxNumAlgoOrders": max_num_algo_orders
            }

    
    def ExchangeMaxNumIcebergOrdersFilter(
            self,
            max_num_iceberg_orders: int = None
    ):
        """
        Description:
        The EXCHANGE_MAX_NUM_ICEBERG_ORDERS filter defines the maximum number of iceberg orders an account is 
        allowed to have open on the exchange.
        """
        return {
            "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",
            "maxNumIcebergOrders": max_num_iceberg_orders
            }

    
    def ExchangeMaxNumOrderListsFilter(
            self,
            max_num_order_lists: int = None
    ):
        """
        Description:
            The EXCHANGE_MAX_NUM_ORDERS filter defines the maximum number of order lists an account is allowed 
            to have open on the exchange. Note that OTOCOs count as one order list.
        """
        return {
            "filterType": "EXCHANGE_MAX_NUM_ORDER_LISTS",
            "maxNumOrderLists": max_num_order_lists
            }
