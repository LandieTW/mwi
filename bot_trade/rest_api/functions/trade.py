
from typing import Union
from typing import Optional

from bot_trade.others.functions import get_data

from collections import defaultdict

from binance_sdk_spot.spot import Spot
from binance_sdk_spot.rest_api.models import \
    OrderTestSideEnum, OrderListOtocoWorkingTypeEnum , OrderListOtocoWorkingSideEnum,\
    OrderListOtocoPendingSideEnum, OrderListOtocoPendingAboveTypeEnum,\
    OrderListOtoWorkingTypeEnum, OrderTestTypeEnum, OrderTestTimeInForceEnum,\
    OrderTestNewOrderRespTypeEnum, OrderTestSelfTradePreventionModeEnum,\
    OrderTestPegPriceTypeEnum, OrderTestPegOffsetTypeEnum, SorOrderTestSideEnum,\
    SorOrderTestTypeEnum, SorOrderTestTimeInForceEnum, SorOrderTestNewOrderRespTypeEnum,\
    SorOrderTestSelfTradePreventionModeEnum, SorOrderSideEnum, SorOrderTypeEnum,\
    SorOrderTimeInForceEnum, SorOrderNewOrderRespTypeEnum, SorOrderSelfTradePreventionModeEnum,\
    OrderCancelReplaceSideEnum, OrderCancelReplaceTypeEnum,\
    OrderCancelReplaceCancelReplaceModeEnum, OrderCancelReplaceTimeInForceEnum,\
    OrderCancelReplaceNewOrderRespTypeEnum, OrderCancelReplaceSelfTradePreventionModeEnum,\
    OrderCancelReplaceCancelRestrictionsEnum, OrderCancelReplaceOrderRateLimitExceededModeEnum,\
    OrderCancelReplacePegPriceTypeEnum, OrderCancelReplacePegOffsetTypeEnum,\
    OrderListOtoPendingSideEnum, OrderListOtoWorkingSideEnum,\
    OrderListOtoPendingTypeEnum, NewOrderSideEnum,\
    NewOrderTypeEnum, OrderListOtocoPendingAbovePegPriceTypeEnum,\
    OrderListOtocoPendingAbovePegOffsetTypeEnum, OrderListOtocoPendingBelowTypeEnum,\
    OrderListOtocoPendingBelowTimeInForceEnum, OrderListOtocoPendingBelowPegPriceTypeEnum,\
    OrderListOtocoPendingBelowPegOffsetTypeEnum, OrderListOtocoNewOrderRespTypeEnum, \
    OrderListOtocoSelfTradePreventionModeEnum, OrderListOtocoWorkingTimeInForceEnum, \
    OrderListOtocoWorkingPegPriceTypeEnum, OrderListOtocoWorkingPegOffsetTypeEnum, \
    OrderListOtocoPendingAboveTimeInForceEnum, OrderListOtoNewOrderRespTypeEnum, \
    OrderListOtoSelfTradePreventionModeEnum, OrderListOtoWorkingTimeInForceEnum, \
    OrderListOtoWorkingPegPriceTypeEnum, OrderListOtoWorkingPegOffsetTypeEnum, \
    OrderListOtoPendingTimeInForceEnum, OrderListOtoPendingPegPriceTypeEnum, \
    OrderListOtoPendingPegOffsetTypeEnum, NewOrderTimeInForceEnum, \
    NewOrderNewOrderRespTypeEnum, NewOrderSelfTradePreventionModeEnum,\
    NewOrderPegPriceTypeEnum, NewOrderPegOffsetTypeEnum, DeleteOrderCancelRestrictionsEnum,\
    OrderListOcoSideEnum, OrderListOcoAboveTypeEnum, OrderListOcoBelowTypeEnum,\
    OrderListOcoAbovePegPriceTypeEnum, OrderListOcoAbovePegOffsetTypeEnum,\
    OrderListOcoBelowTimeInForceEnum, OrderListOcoBelowPegPriceTypeEnum,\
    OrderListOcoBelowPegOffsetTypeEnum, OrderListOcoNewOrderRespTypeEnum,\
    OrderListOcoSelfTradePreventionModeEnum


def sor_order(
        client: Spot,
        symbol: Union[str, None],
        side: Union[SorOrderSideEnum, None],
        type: Union[SorOrderTypeEnum, None],
        quantity: Union[float, None],
        time_in_force: Optional[SorOrderTimeInForceEnum] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        new_order_resp_type: Optional[SorOrderNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[SorOrderSelfTradePreventionModeEnum] = None,
    ) -> defaultdict:
    """
    Description:
        Places an order using smart order routing (SOR).
    """
    return get_data(
        client.rest_api.sor_order(
            symbol=symbol,
            side=side.value if side else None,
            type=type.value if type else None,
            quantity=quantity,
            time_in_force=time_in_force.value if time_in_force else None,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type.value if new_order_resp_type else None,
            self_trade_prevention_mode=self_trade_prevention_mode.value \
                if self_trade_prevention_mode else None,
        )
    )


def sor_order_test(
        client: Spot,
        symbol: Union[str, None],
        side: Union[SorOrderTestSideEnum, None],
        type: Union[SorOrderTestTypeEnum, None],
        quantity: Union[float, None],
        compute_commission_rates: Optional[bool] = None,
        time_in_force: Optional[SorOrderTestTimeInForceEnum] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        new_order_resp_type: Optional[SorOrderTestNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[SorOrderTestSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Test new order creation and signature/recvWindow using smart order routing (SOR).
        Creates and validates a new order but does not send it into the matching engine.
    """
    return get_data(
        client.rest_api.sor_order_test(
            symbol=symbol,
            side=side.value if side else None,
            type=type.value if type else None,
            quantity=quantity,
            compute_commission_rates=compute_commission_rates,
            time_in_force=time_in_force.value if time_in_force else None,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type.value if new_order_resp_type else None,
            self_trade_prevention_mode=self_trade_prevention_mode.value \
                if self_trade_prevention_mode else None,
            recv_window=recv_window
        )
    )


def order_cancel_replace(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderCancelReplaceSideEnum, None],
        type: Union[OrderCancelReplaceTypeEnum, None],
        cancel_replace_mode: Union[OrderCancelReplaceCancelReplaceModeEnum, None],
        time_in_force: Optional[OrderCancelReplaceTimeInForceEnum] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        price: Optional[float] = None,
        cancel_new_client_order_id: Optional[str] = None,
        cancel_orig_client_order_id: Optional[str] = None,
        cancel_order_id: Optional[int] = None,
        new_client_order_id: Optional[str] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        new_order_resp_type: Optional[OrderCancelReplaceNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[
            OrderCancelReplaceSelfTradePreventionModeEnum] = None,
        cancel_restrictions: Optional[OrderCancelReplaceCancelRestrictionsEnum] = None,
        order_rate_limit_exceeded_mode: Optional[
            OrderCancelReplaceOrderRateLimitExceededModeEnum] = None,
        peg_price_type: Optional[OrderCancelReplacePegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderCancelReplacePegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancels an existing order and places a new order on the same symbol.
    """
    return get_data(
        client.rest_api.order_cancel_replace(
            symbol=symbol,
            side=side.value if side else None,
            type=type.value if type else None,
            cancel_replace_mode=cancel_replace_mode.value if cancel_replace_mode else None,
            time_in_force=time_in_force.value if time_in_force else None,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            cancel_new_client_order_id=cancel_new_client_order_id,
            cancel_orig_client_order_id=cancel_orig_client_order_id,
            cancel_order_id=cancel_order_id,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type.value if new_order_resp_type else None,
            self_trade_prevention_mode=self_trade_prevention_mode.value \
                if self_trade_prevention_mode else None,
            cancel_restrictions=cancel_restrictions.value if cancel_restrictions else None,
            order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode.value \
                if order_rate_limit_exceeded_mode else None,
            peg_price_type=peg_price_type.value if peg_price_type else None,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type.value if peg_offset_type else None,
            recv_window=recv_window
        )
    )


def order_test(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderTestSideEnum, None],
        type: Union[OrderTestTypeEnum, None],
        compute_commission_rates: Optional[bool] = None,
        time_in_force: Optional[OrderTestTimeInForceEnum] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        new_order_resp_type: Optional[OrderTestNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderTestSelfTradePreventionModeEnum] = None,
        peg_price_type: Optional[OrderTestPegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderTestPegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Test new order creation and signature/recvWindow long.
        Creates and validates a new order but does not send it into the matching engine.
    """
    return get_data(
        client.rest_api.order_test(
            symbol=symbol,
            side=side.value if side else None,
            type=type.value if type else None,
            compute_commission_rates=compute_commission_rates,
            time_in_force=time_in_force.value if time_in_force else None,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type.value if new_order_resp_type else None,
            self_trade_prevention_mode=self_trade_prevention_mode.value \
                if self_trade_prevention_mode else None,
            peg_price_type=peg_price_type.value if peg_price_type else None,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type.value if peg_offset_type else None,
            recv_window=recv_window
        )
    )


def order_list_oco(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderListOcoSideEnum, None],
        quantity: Union[float, None],
        above_type: Union[OrderListOcoAboveTypeEnum, None],
        below_type: Union[OrderListOcoBelowTypeEnum, None],
        list_client_order_id: Optional[str] = None,
        above_client_order_id: Optional[str] = None,
        above_iceberg_qty: Optional[int] = None,
        above_price: Optional[float] = None,
        above_stop_price: Optional[float] = None,
        above_trailing_delta: Optional[int] = None,
        above_time_in_force: Optional[float] = None,
        above_strategy_id: Optional[int] = None,
        above_strategy_type: Optional[int] = None,
        above_peg_price_type: Optional[OrderListOcoAbovePegPriceTypeEnum] = None,
        above_peg_offset_type: Optional[OrderListOcoAbovePegOffsetTypeEnum] = None,
        above_peg_offset_value: Optional[int] = None,
        below_client_order_id: Optional[str] = None,
        below_iceberg_qty: Optional[int] = None,
        below_price: Optional[float] = None,
        below_stop_price: Optional[float] = None,
        below_trailing_delta: Optional[int] = None,
        below_time_in_force: Optional[OrderListOcoBelowTimeInForceEnum] = None,
        below_strategy_id: Optional[int] = None,
        below_strategy_type: Optional[int] = None,
        below_peg_price_type: Optional[OrderListOcoBelowPegPriceTypeEnum] = None,
        below_peg_offset_type: Optional[OrderListOcoBelowPegOffsetTypeEnum] = None,
        below_peg_offset_value: Optional[int] = None,
        new_order_resp_type: Optional[OrderListOcoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListOcoSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
) -> defaultdict:
    """
    Description:
        Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately 
        cancels the other.

        * An OCO has 2 orders called the **above order** and **below order**.
        * One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and 
        the other must be `STOP_LOSS` or `STOP_LOSS_LIMIT` order.
        * Price restrictions
          * If the OCO is on the `SELL` side:
            * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price >  
            `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
            * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
          * If the OCO is on the `BUY` side:
            * `LIMIT_MAKER/TAKE_PROFIT_LIMIT price` < Last Traded Price < `stopPrice`
            * `TAKE_PROFIT stopPrice` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
        * OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the 
        `MAX_NUM_ORDERS` filter.
    """
    return get_data(
        client.rest_api.order_list_oco(
            symbol=symbol,
            side=side.value if side else None,
            quantity=quantity,
            above_type=above_type.value if above_type else None,
            below_type=below_type.value if below_type else None,
            list_client_order_id=list_client_order_id,
            above_client_order_id=above_client_order_id,
            above_iceberg_qty=above_iceberg_qty,
            above_price=above_price,
            above_stop_price=above_stop_price,
            above_trailing_delta=above_trailing_delta,
            above_time_in_force=above_time_in_force,
            above_strategy_id=above_strategy_id,
            above_strategy_type=above_strategy_type,
            above_peg_price_type=above_peg_price_type,
            above_peg_offset_type=above_peg_offset_type,
            above_peg_offset_value=above_peg_offset_value,
            below_client_order_id=below_client_order_id,
            below_iceberg_qty=below_iceberg_qty,
            below_price=below_price,
            below_stop_price=below_stop_price,
            below_trailing_delta=below_trailing_delta,
            below_time_in_force=below_time_in_force,
            below_strategy_id=below_strategy_id,
            below_strategy_type=below_strategy_type,
            below_peg_price_type=below_peg_price_type,
            below_peg_offset_type=below_peg_offset_type,
            below_peg_offset_value=below_peg_offset_value,
            new_order_resp_type=new_order_resp_type.value if new_order_resp_type else None,
            self_trade_prevention_mode=self_trade_prevention_mode.value
                if self_trade_prevention_mode else None,
            recv_window=recv_window
        )
    )


def order_list_otoco(
        client: Spot,
        symbol: Union[str, None],
        working_type: Union[OrderListOtocoWorkingTypeEnum, None],
        working_side: Union[OrderListOtocoWorkingSideEnum, None],
        working_price: Union[float, None],
        working_quantity: Union[float, None],
        pending_side: Union[OrderListOtocoPendingSideEnum, None],
        pending_quantity: Union[float, None],
        pending_above_type: Union[OrderListOtocoPendingAboveTypeEnum, None],
        list_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderListOtocoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListOtocoSelfTradePreventionModeEnum] = None,
        working_client_order_id: Optional[str] = None,
        working_iceberg_qty: Optional[float] = None,
        working_time_in_force: Optional[OrderListOtocoWorkingTimeInForceEnum] = None,
        working_strategy_id: Optional[int] = None,
        working_strategy_type: Optional[int] = None,
        working_peg_price_type: Optional[OrderListOtocoWorkingPegPriceTypeEnum] = None,
        working_peg_offset_type: Optional[OrderListOtocoWorkingPegOffsetTypeEnum] = None,
        working_peg_offset_value: Optional[int] = None,
        pending_above_client_order_id: Optional[str] = None,
        pending_above_price: Optional[float] = None,
        pending_above_stop_price: Optional[float] = None,
        pending_above_trailing_delta: Optional[float] = None,
        pending_above_iceberg_qty: Optional[float] = None,
        pending_above_time_in_force: Optional[OrderListOtocoPendingAboveTimeInForceEnum] = None,
        pending_above_strategy_id: Optional[int] = None,
        pending_above_strategy_type: Optional[int] = None,
        pending_above_peg_price_type: Optional[
            OrderListOtocoPendingAbovePegPriceTypeEnum] = None,
        pending_above_peg_offset_type: Optional[
            OrderListOtocoPendingAbovePegOffsetTypeEnum] = None,
        pending_above_peg_offset_value: Optional[int] = None,
        pending_below_type: Optional[OrderListOtocoPendingBelowTypeEnum] = None,
        pending_below_client_order_id: Optional[str] = None,
        pending_below_price: Optional[float] = None,
        pending_below_stop_price: Optional[float] = None,
        pending_below_trailing_delta: Optional[float] = None,
        pending_below_iceberg_qty: Optional[float] = None,
        pending_below_time_in_force: Optional[OrderListOtocoPendingBelowTimeInForceEnum] = None,
        pending_below_strategy_id: Optional[int] = None,
        pending_below_strategy_type: Optional[int] = None,
        pending_below_peg_price_type: Optional[
            OrderListOtocoPendingBelowPegPriceTypeEnum] = None,
        pending_below_peg_offset_type: Optional[
            OrderListOtocoPendingBelowPegOffsetTypeEnum] = None,
        pending_below_peg_offset_value: Optional[int] = None,
        recv_window: Optional[int] = None, 
    ) -> defaultdict:
    """
    Description:
        Place an OTOCO.
        * An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
        * The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. 
        Initially, only the working order goes on the order book.
        * The behavior of the working order is the same as the [OTO]
        (#new-order-list---oto-trade).
        * OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. 
        The pending orders are only placed on the order book when the working order gets 
        **fully filled**.
        * The rules of the pending above and pending below follow the same rules as the 
        [Order list OCO](#new-order-list---oco-trade).
        * OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` 
        filter.
    """
    return get_data(
        client.rest_api.order_list_otoco(
            symbol=symbol,
            working_type=working_type.value if working_type else None,
            working_side=working_side.value if working_side else None,
            working_price=working_price,
            working_quantity=working_quantity,
            pending_side=pending_side.value if pending_side else None,
            pending_quantity=pending_quantity,
            pending_above_type=pending_above_type.value if pending_above_type else None,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            working_client_order_id=working_client_order_id,
            working_iceberg_qty=working_iceberg_qty,
            working_time_in_force=working_time_in_force,
            working_strategy_id=working_strategy_id,
            working_strategy_type=working_strategy_type,
            working_peg_price_type=working_peg_price_type,
            working_peg_offset_type=working_peg_offset_type,
            working_peg_offset_value=working_peg_offset_value,
            pending_above_client_order_id=pending_above_client_order_id,
            pending_above_price=pending_above_price,
            pending_above_stop_price=pending_above_stop_price,
            pending_above_trailing_delta=pending_above_trailing_delta,
            pending_above_iceberg_qty=pending_above_iceberg_qty,
            pending_above_time_in_force=pending_above_time_in_force,
            pending_above_strategy_id=pending_above_strategy_id,
            pending_above_strategy_type=pending_above_strategy_type,
            pending_above_peg_price_type=pending_above_peg_price_type,
            pending_above_peg_offset_type=pending_above_peg_offset_type,
            pending_above_peg_offset_value=pending_above_peg_offset_value,
            pending_below_type=pending_below_type.value if pending_below_type else None,
            pending_below_client_order_id=pending_below_client_order_id,
            pending_below_price=pending_below_price,
            pending_below_stop_price=pending_below_stop_price,
            pending_below_trailing_delta=pending_below_trailing_delta,
            pending_below_iceberg_qty=pending_below_iceberg_qty,
            pending_below_time_in_force=pending_below_time_in_force,
            pending_below_strategy_id=pending_below_strategy_id,
            pending_below_strategy_type=pending_below_strategy_type,
            pending_below_peg_price_type=pending_below_peg_price_type,
            pending_below_peg_offset_type=pending_below_peg_offset_type,
            pending_below_peg_offset_value=pending_below_peg_offset_value,
            recv_window=recv_window
        )
    )


def order_list_oto(
        client: Spot,
        symbol: Union[str, None],
        working_type: Union[OrderListOtoWorkingTypeEnum, None],
        working_side: Union[OrderListOtoWorkingSideEnum, None],
        working_price: Union[float, None],
        working_quantity: Union[float, None],
        pending_type: Union[OrderListOtoPendingTypeEnum, None],
        pending_side: Union[OrderListOtoPendingSideEnum, None],
        pending_quantity: Union[float, None],
        list_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderListOtoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[
            OrderListOtoSelfTradePreventionModeEnum
        ] = None,
        working_client_order_id: Optional[str] = None,
        working_iceberg_qty: Optional[float] = None,
        working_time_in_force: Optional[OrderListOtoWorkingTimeInForceEnum] = None,
        working_strategy_id: Optional[int] = None,
        working_strategy_type: Optional[int] = None,
        working_peg_price_type: Optional[OrderListOtoWorkingPegPriceTypeEnum] = None,
        working_peg_offset_type: Optional[OrderListOtoWorkingPegOffsetTypeEnum] = None,
        working_peg_offset_value: Optional[int] = None,
        pending_client_order_id: Optional[str] = None,
        pending_price: Optional[float] = None,
        pending_stop_price: Optional[float] = None,
        pending_trailing_delta: Optional[float] = None,
        pending_iceberg_qty: Optional[float] = None,
        pending_time_in_force: Optional[OrderListOtoPendingTimeInForceEnum] = None,
        pending_strategy_id: Optional[int] = None,
        pending_strategy_type: Optional[int] = None,
        pending_peg_price_type: Optional[OrderListOtoPendingPegPriceTypeEnum] = None,
        pending_peg_offset_type: Optional[OrderListOtoPendingPegOffsetTypeEnum] = None,
        pending_peg_offset_value: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Place an OTO.
        * An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
        * The first order is called the **working order** and must be `LIMIT` or 
        `LIMIT_MAKER`. Initially, only the working order goes on the order book.
        * The second order is called the **pending order**. It can be any order type except 
        for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed 
        on the order book when the working order gets **fully filled**.
        * If either the working order or the pending order is cancelled individually, the 
        other order in the order list will also be canceled or expired.
        * When the order list is placed, if the working order gets **immediately fully 
        filled**, the placement response will show the working order as `FILLED` but the 
        pending order will still appear as `PENDING_NEW`. You need to query the status of 
        the pending order again to see its updated status.
        * OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and 
        `MAX_NUM_ORDERS` filter.
    """
    return get_data(
        client.rest_api.order_list_oto(
            symbol=symbol,
            working_type=working_type.value if working_type else None,
            working_side=working_side.value if working_side else None,
            working_price=working_price,
            working_quantity=working_quantity,
            pending_type=pending_type.value if pending_type else None,
            pending_side=pending_side.value if pending_side else None,
            pending_quantity=pending_quantity,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            working_client_order_id=working_client_order_id,
            working_iceberg_qty=working_iceberg_qty,
            working_time_in_force=working_time_in_force,
            working_strategy_id=working_strategy_id,
            working_strategy_type=working_strategy_type,
            working_peg_price_type=working_peg_price_type,
            working_peg_offset_type=working_peg_offset_type,
            working_peg_offset_value=working_peg_offset_value,
            pending_client_order_id=pending_client_order_id,
            pending_price=pending_price,
            pending_stop_price=pending_stop_price,
            pending_trailing_delta=pending_trailing_delta,
            pending_iceberg_qty=pending_iceberg_qty,
            pending_time_in_force=pending_time_in_force,
            pending_strategy_id=pending_strategy_id,
            pending_strategy_type=pending_strategy_type,
            pending_peg_price_type=pending_peg_price_type,
            pending_peg_offset_type=pending_peg_offset_type,
            pending_peg_offset_value=pending_peg_offset_value,
            recv_window=recv_window
        )
    )


def order_amend_keep_priority(
        client: Spot,
        symbol: Union[str, None],
        new_qty: Union[float, None],
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Reduce the quantity of an existing open order.
    """
    return get_data(
        client.rest_api.order_amend_keep_priority(
            symbol=symbol,
            new_qty=new_qty,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window
        )
    )


def new_order(
        client: Spot,
        symbol: Union[str, None],
        side: Union[NewOrderSideEnum, None],
        type: Union[NewOrderTypeEnum, None],
        time_in_force: Optional[NewOrderTimeInForceEnum] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        new_order_resp_type: Optional[NewOrderNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[
            NewOrderSelfTradePreventionModeEnum
        ] = None,
        peg_price_type: Optional[NewOrderPegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[NewOrderPegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Send in a new order.
    """
    return get_data(
        client.rest_api.new_order(
            symbol=symbol,
            side=side.value if side else None,
            type=type.value if type else None,
            time_in_force=time_in_force.value if time_in_force else None,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type.value if new_order_resp_type else None,
            self_trade_prevention_mode=self_trade_prevention_mode.value
                    if self_trade_prevention_mode else None,
            peg_price_type=peg_price_type.value if peg_price_type else None,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type.value if peg_offset_type else None,
            recv_window=recv_window
        )
    )


def delete_order(
        client: Spot,
        symbol: Union[str, None],
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        cancel_restrictions: Optional[DeleteOrderCancelRestrictionsEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancel an active order.
    """
    return get_data(
        client.rest_api.delete_order(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            cancel_restrictions=cancel_restrictions.value if cancel_restrictions else None,
            recv_window=recv_window
        )
    )


def delete_order_list(
        client: Spot,
        symbol: Union[str, None],
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        cancel_restrictions: Optional[DeleteOrderCancelRestrictionsEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancel an active order list.
    """
    return get_data(
        client.rest_api.delete_order_list(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            cancel_restrictions=cancel_restrictions.value if cancel_restrictions else None,
            recv_window=recv_window
        )
)


def delete_open_orders(
        client: Spot,
        symbol: Union[str, None],
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancel all active orders on a symbol.
    """
    return get_data(
        client.rest_api.delete_open_orders(
            symbol=symbol,
            recv_window=recv_window
        )
)