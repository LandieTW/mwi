
import asyncio

from typing import Optional, Union

from bot_trade.others.functions import get_data

from collections import defaultdict

from binance_sdk_spot.spot import Spot

from binance_sdk_spot.websocket_api.models import OrderListPlaceOtoWorkingTypeEnum, \
    OrderListPlaceOtoWorkingSideEnum, OrderListPlaceOtoPendingTypeEnum, \
    OrderListPlaceOtoPendingSideEnum, OrderListPlaceOtoNewOrderRespTypeEnum, \
    OrderListPlaceOtoSelfTradePreventionModeEnum, OrderListPlaceOtoWorkingTimeInForceEnum,\
    OrderListPlaceOtoWorkingPegPriceTypeEnum, OrderListPlaceOtoWorkingPegOffsetTypeEnum,\
    OrderListPlaceOtoPendingTimeInForceEnum, OrderListPlaceOtoPendingPegOffsetTypeEnum,\
    OrderListPlaceOtoPendingPegPriceTypeEnum, OrderListPlaceOcoSideEnum,\
    OrderListPlaceOcoAboveTypeEnum, OrderListPlaceOcoBelowTypeEnum,\
    OrderListPlaceOcoAbovePegPriceTypeEnum, OrderListPlaceOcoAbovePegOffsetTypeEnum,\
    OrderListPlaceOcoBelowTimeInForceEnum, OrderListPlaceOcoBelowPegPriceTypeEnum,\
    OrderListPlaceOcoBelowPegOffsetTypeEnum, OrderListPlaceOcoNewOrderRespTypeEnum,\
    OrderListPlaceOcoSelfTradePreventionModeEnum, OrderCancelCancelRestrictionsEnum,\
    OrderCancelReplaceCancelReplaceModeEnum, OrderCancelReplaceSideEnum,\
    OrderCancelReplaceTypeEnum, OrderCancelReplaceTimeInForceEnum,\
    OrderCancelReplaceNewOrderRespTypeEnum, OrderCancelReplaceSelfTradePreventionModeEnum,\
    OrderCancelReplaceCancelRestrictionsEnum, OrderCancelReplaceOrderRateLimitExceededModeEnum,\
    OrderCancelReplacePegPriceTypeEnum, OrderCancelReplacePegOffsetTypeEnum,\
    SorOrderTestSideEnum, SorOrderTestTypeEnum, SorOrderTestTimeInForceEnum,\
    SorOrderTestNewOrderRespTypeEnum, SorOrderTestSelfTradePreventionModeEnum,\
    SorOrderPlaceSideEnum, SorOrderPlaceTypeEnum, SorOrderPlaceTimeInForceEnum,\
    SorOrderPlaceNewOrderRespTypeEnum, SorOrderPlaceSelfTradePreventionModeEnum,\
    OrderTestSideEnum, OrderTestTypeEnum, OrderTestTimeInForceEnum, \
    OrderTestNewOrderRespTypeEnum, OrderTestSelfTradePreventionModeEnum,\
    OrderTestPegPriceTypeEnum, OrderTestPegOffsetTypeEnum, OrderPlaceSideEnum,\
    OrderPlaceTypeEnum, OrderPlaceTimeInForceEnum, OrderPlaceNewOrderRespTypeEnum,\
    OrderPlaceSelfTradePreventionModeEnum, OrderPlacePegPriceTypeEnum, \
    OrderPlacePegOffsetTypeEnum, OrderListPlaceSideEnum, OrderListPlaceStopLimitTimeInForceEnum,\
    OrderListPlaceNewOrderRespTypeEnum, OrderListPlaceSelfTradePreventionModeEnum,\
    OrderListPlaceOtocoWorkingTypeEnum, OrderListPlaceOtocoWorkingSideEnum,\
    OrderListPlaceOtocoPendingSideEnum, OrderListPlaceOtocoPendingAboveTypeEnum,\
    OrderListPlaceOtocoNewOrderRespTypeEnum, OrderListPlaceOtocoSelfTradePreventionModeEnum,\
    OrderListPlaceOtocoWorkingTimeInForceEnum, OrderListPlaceOtocoWorkingPegPriceTypeEnum,\
    OrderListPlaceOtocoWorkingPegOffsetTypeEnum, OrderListPlaceOtocoPendingAboveTimeInForceEnum,\
    OrderListPlaceOtocoPendingAbovePegPriceTypeEnum, OrderListPlaceOtocoPendingAbovePegOffsetTypeEnum,\
    OrderListPlaceOtocoPendingBelowTypeEnum, OrderListPlaceOtocoPendingBelowTimeInForceEnum,\
    OrderListPlaceOtocoPendingBelowPegPriceTypeEnum, OrderListPlaceOtocoPendingBelowPegOffsetTypeEnum


async def order_list_place_oto(
        client: Spot,
        symbol: Union[str, None],
        working_type: Union[OrderListPlaceOtoWorkingTypeEnum, None],
        working_side: Union[OrderListPlaceOtoWorkingSideEnum, None],
        working_price: Union[float, None],
        working_quantity: Union[float, None],
        pending_type: Union[OrderListPlaceOtoPendingTypeEnum, None],
        pending_side: Union[OrderListPlaceOtoPendingSideEnum, None],
        pending_quantity: Union[float, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderListPlaceOtoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListPlaceOtoSelfTradePreventionModeEnum] = None,
        working_client_order_id: Optional[str] = None,
        working_iceberg_qty: Optional[float] = None,
        working_time_in_force: Optional[OrderListPlaceOtoWorkingTimeInForceEnum] = None,
        working_strategy_id: Optional[int] = None,
        working_strategy_type: Optional[int] = None,
        working_peg_price_type: Optional[OrderListPlaceOtoWorkingPegPriceTypeEnum] = None,
        working_peg_offset_type: Optional[OrderListPlaceOtoWorkingPegOffsetTypeEnum] = None,
        working_peg_offset_value: Optional[int] = None,
        pending_client_order_id: Optional[str] = None,
        pending_price: Optional[float] = None,
        pending_stop_price: Optional[float] = None,
        pending_trailing_delta: Optional[float] = None,
        pending_iceberg_qty: Optional[float] = None,
        pending_time_in_force: Optional[OrderListPlaceOtoPendingTimeInForceEnum] = None,
        pending_strategy_id: Optional[int] = None,
        pending_strategy_type: Optional[int] = None,
        pending_peg_offset_type: Optional[OrderListPlaceOtoPendingPegOffsetTypeEnum] = None,
        pending_peg_price_type: Optional[OrderListPlaceOtoPendingPegPriceTypeEnum] = None,
        pending_peg_offset_value: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Get current average price for a symbol.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_list_place_oto(
            symbol=symbol,
            working_type=working_type,
            working_side=working_side,
            working_price=working_price,
            working_quantity=working_quantity,
            pending_type=pending_type,
            pending_side=pending_side,
            pending_quantity=pending_quantity,
            id=id,
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
            pending_peg_offset_type=pending_peg_offset_type,
            pending_peg_price_type=pending_peg_price_type,
            pending_peg_offset_value=pending_peg_offset_value,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_list_place_oto(
        client: Spot,
        symbol: Union[str, None],
        working_type: Union[OrderListPlaceOtoWorkingTypeEnum, None],
        working_side: Union[OrderListPlaceOtoWorkingSideEnum, None],
        working_price: Union[float, None],
        working_quantity: Union[float, None],
        pending_type: Union[OrderListPlaceOtoPendingTypeEnum, None],
        pending_side: Union[OrderListPlaceOtoPendingSideEnum, None],
        pending_quantity: Union[float, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderListPlaceOtoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListPlaceOtoSelfTradePreventionModeEnum] = None,
        working_client_order_id: Optional[str] = None,
        working_iceberg_qty: Optional[float] = None,
        working_time_in_force: Optional[OrderListPlaceOtoWorkingTimeInForceEnum] = None,
        working_strategy_id: Optional[int] = None,
        working_strategy_type: Optional[int] = None,
        working_peg_price_type: Optional[OrderListPlaceOtoWorkingPegPriceTypeEnum] = None,
        working_peg_offset_type: Optional[OrderListPlaceOtoWorkingPegOffsetTypeEnum] = None,
        working_peg_offset_value: Optional[int] = None,
        pending_client_order_id: Optional[str] = None,
        pending_price: Optional[float] = None,
        pending_stop_price: Optional[float] = None,
        pending_trailing_delta: Optional[float] = None,
        pending_iceberg_qty: Optional[float] = None,
        pending_time_in_force: Optional[OrderListPlaceOtoPendingTimeInForceEnum] = None,
        pending_strategy_id: Optional[int] = None,
        pending_strategy_type: Optional[int] = None,
        pending_peg_offset_type: Optional[OrderListPlaceOtoPendingPegOffsetTypeEnum] = None,
        pending_peg_price_type: Optional[OrderListPlaceOtoPendingPegPriceTypeEnum] = None,
        pending_peg_offset_value: Optional[int] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_list_place_oto(
            client=client,
            symbol=symbol,
            working_type=working_type,
            working_side=working_side,
            working_price=working_price,
            working_quantity=working_quantity,
            pending_type=pending_type,
            pending_side=pending_side,
            pending_quantity=pending_quantity,
            id=id,
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
            pending_peg_offset_type=pending_peg_offset_type,
            pending_peg_price_type=pending_peg_price_type,
            pending_peg_offset_value=pending_peg_offset_value,
            recv_window=recv_window
        )
    )


async def order_list_place_oco(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderListPlaceOcoSideEnum, None],
        quantity: Union[float, None],
        above_type: Union[OrderListPlaceOcoAboveTypeEnum, None],
        below_type: Union[OrderListPlaceOcoBelowTypeEnum, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        above_client_order_id: Optional[str] = None,
        above_iceberg_qty: Optional[int] = None,
        above_price: Optional[float] = None,
        above_stop_price: Optional[float] = None,
        above_trailing_delta: Optional[int] = None,
        above_time_in_force: Optional[float] = None,
        above_strategy_id: Optional[int] = None,
        above_strategy_type: Optional[int] = None,
        above_peg_price_type: Optional[OrderListPlaceOcoAbovePegPriceTypeEnum] = None,
        above_peg_offset_type: Optional[OrderListPlaceOcoAbovePegOffsetTypeEnum] = None,
        above_peg_offset_value: Optional[int] = None,
        below_client_order_id: Optional[str] = None,
        below_iceberg_qty: Optional[int] = None,
        below_price: Optional[float] = None,
        below_stop_price: Optional[float] = None,
        below_trailing_delta: Optional[int] = None,
        below_time_in_force: Optional[OrderListPlaceOcoBelowTimeInForceEnum] = None,
        below_strategy_id: Optional[int] = None,
        below_strategy_type: Optional[int] = None,
        below_peg_price_type: Optional[OrderListPlaceOcoBelowPegPriceTypeEnum] = None,
        below_peg_offset_type: Optional[OrderListPlaceOcoBelowPegOffsetTypeEnum] = None,
        below_peg_offset_value: Optional[int] = None,
        new_order_resp_type: Optional[OrderListPlaceOcoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListPlaceOcoSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Send in an one-cancels-the-other (OCO) pair, where activation of one 
        order immediately cancels the other.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_list_place_oco(
            symbol=symbol,
            side=side,
            quantity=quantity,
            above_type=above_type,
            below_type=below_type,
            id=id,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
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
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_list_place_oco(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderListPlaceOcoSideEnum, None],
        quantity: Union[float, None],
        above_type: Union[OrderListPlaceOcoAboveTypeEnum, None],
        below_type: Union[OrderListPlaceOcoBelowTypeEnum, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        above_client_order_id: Optional[str] = None,
        above_iceberg_qty: Optional[int] = None,
        above_price: Optional[float] = None,
        above_stop_price: Optional[float] = None,
        above_trailing_delta: Optional[int] = None,
        above_time_in_force: Optional[float] = None,
        above_strategy_id: Optional[int] = None,
        above_strategy_type: Optional[int] = None,
        above_peg_price_type: Optional[OrderListPlaceOcoAbovePegPriceTypeEnum] = None,
        above_peg_offset_type: Optional[OrderListPlaceOcoAbovePegOffsetTypeEnum] = None,
        above_peg_offset_value: Optional[int] = None,
        below_client_order_id: Optional[str] = None,
        below_iceberg_qty: Optional[int] = None,
        below_price: Optional[float] = None,
        below_stop_price: Optional[float] = None,
        below_trailing_delta: Optional[int] = None,
        below_time_in_force: Optional[OrderListPlaceOcoBelowTimeInForceEnum] = None,
        below_strategy_id: Optional[int] = None,
        below_strategy_type: Optional[int] = None,
        below_peg_price_type: Optional[OrderListPlaceOcoBelowPegPriceTypeEnum] = None,
        below_peg_offset_type: Optional[OrderListPlaceOcoBelowPegOffsetTypeEnum] = None,
        below_peg_offset_value: Optional[int] = None,
        new_order_resp_type: Optional[OrderListPlaceOcoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListPlaceOcoSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_list_place_oco(
            client=client,
            symbol=symbol,
            side=side,
            quantity=quantity,
            above_type=above_type,
            below_type=below_type,
            id=id,
            list_client_order_id=list_client_order_id,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
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
            recv_window=recv_window
        )
    )


async def order_list_cancel(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_list_id: Optional[int] = None,
        list_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancel an active order list.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_list_cancel(
            symbol=symbol,
            order_list_id=order_list_id,
            id=id,
            list_client_order_id=list_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_list_cancel(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_list_id: Optional[int] = None,
        list_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_list_cancel(
            client=client,
            symbol=symbol,
            order_list_id=order_list_id,
            id=id,
            list_client_order_id=list_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window
        )
    )


async def order_cancel(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        cancel_restrictions: Optional[OrderCancelCancelRestrictionsEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancel an active order.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_cancel(
            symbol=symbol,
            id=id,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            cancel_restrictions=cancel_restrictions,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_cancel(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        cancel_restrictions: Optional[OrderCancelCancelRestrictionsEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_cancel(
            client=client,
            symbol=symbol,
            id=id,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            cancel_restrictions=cancel_restrictions,
            recv_window=recv_window
        )
    )


async def order_cancel_replace(
        client: Spot,
        symbol: Union[str, None],
        cancel_replace_mode: Union[OrderCancelReplaceCancelReplaceModeEnum, None],
        side: Union[OrderCancelReplaceSideEnum, None],
        type: Union[OrderCancelReplaceTypeEnum, None],
        id: Optional[str] = None,
        cancel_order_id: Optional[int] = None,
        cancel_orig_client_order_id: Optional[str] = None,
        cancel_new_client_order_id: Optional[str] = None,
        time_in_force: Optional[OrderCancelReplaceTimeInForceEnum] = None,
        price: Optional[float] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderCancelReplaceNewOrderRespTypeEnum] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[float] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
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
        Cancel an existing order and immediately place a new order instead of the canceled one.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_cancel_replace(
            symbol=symbol,
            cancel_replace_mode=cancel_replace_mode,
            side=side,
            type=type,
            id=id,
            cancel_order_id=cancel_order_id,
            cancel_orig_client_order_id=cancel_orig_client_order_id,
            cancel_new_client_order_id=cancel_new_client_order_id,
            time_in_force=time_in_force,
            price=price,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            cancel_restrictions=cancel_restrictions,
            order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode,
            peg_price_type=peg_price_type,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_cancel_replace(
        client: Spot,
        symbol: Union[str, None],
        cancel_replace_mode: Union[OrderCancelReplaceCancelReplaceModeEnum, None],
        side: Union[OrderCancelReplaceSideEnum, None],
        type: Union[OrderCancelReplaceTypeEnum, None],
        id: Optional[str] = None,
        cancel_order_id: Optional[int] = None,
        cancel_orig_client_order_id: Optional[str] = None,
        cancel_new_client_order_id: Optional[str] = None,
        time_in_force: Optional[OrderCancelReplaceTimeInForceEnum] = None,
        price: Optional[float] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderCancelReplaceNewOrderRespTypeEnum] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[float] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[
            OrderCancelReplaceSelfTradePreventionModeEnum] = None,
        cancel_restrictions: Optional[OrderCancelReplaceCancelRestrictionsEnum] = None,
        order_rate_limit_exceeded_mode: Optional[
            OrderCancelReplaceOrderRateLimitExceededModeEnum] = None,
        peg_price_type: Optional[OrderCancelReplacePegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderCancelReplacePegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_cancel_replace(
            client=client,
            symbol=symbol,
            cancel_replace_mode=cancel_replace_mode,
            side=side,
            type=type,
            id=id,
            cancel_order_id=cancel_order_id,
            cancel_orig_client_order_id=cancel_orig_client_order_id,
            cancel_new_client_order_id=cancel_new_client_order_id,
            time_in_force=time_in_force,
            price=price,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            cancel_restrictions=cancel_restrictions,
            order_rate_limit_exceeded_mode=order_rate_limit_exceeded_mode,
            peg_price_type=peg_price_type,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type,
            recv_window=recv_window            
        )
    )


async def order_amend_keep_priority(
        client: Spot,
        symbol: Union[str, None],
        new_qty: Union[float, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Reduce the quantity of an existing open order.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_amend_keep_priority(
            symbol=symbol,
            new_qty=new_qty,
            id=id,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_amend_keep_priority(
        client: Spot,
        symbol: Union[str, None],
        new_qty: Union[float, None],
        id: Optional[str] = None,
        order_id: Optional[int] = None,
        orig_client_order_id: Optional[str] = None,
        new_client_order_id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_amend_keep_priority(
            client=client,
            symbol=symbol,
            new_qty=new_qty,
            id=id,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window          
        )
    )


async def open_orders_cancel_all(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Cancel all open orders on a symbol.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.open_orders_cancel_all(
            symbol=symbol,
            id=id,
            recv_window=recv_window
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_open_orders_cancel_all(
        client: Spot,
        symbol: Union[str, None],
        id: Optional[str] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        open_orders_cancel_all(
            client=client,
            symbol=symbol,
            id=id,
            recv_window=recv_window          
        )
    )


async def sor_order_test(
        client: Spot,
        symbol: Union[str, None],
        side: Union[SorOrderTestSideEnum, None],
        type: Union[SorOrderTestTypeEnum, None],
        quantity: Union[float, None],
        id: Optional[str] = None,
        compute_commission_rates: Optional[bool] = None,
        time_in_force: Optional[SorOrderTestTimeInForceEnum] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[SorOrderTestNewOrderRespTypeEnum] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[SorOrderTestSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Test new order creation and signature/recvWindow using smart order routing (SOR).
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.sor_order_test(
            symbol=symbol,
            side=side,
            type=type,
            quantity=quantity,
            id=id,
            compute_commission_rates=compute_commission_rates,
            time_in_force=time_in_force,
            price=price,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_sor_order_test(
        client: Spot,
        symbol: Union[str, None],
        side: Union[SorOrderTestSideEnum, None],
        type: Union[SorOrderTestTypeEnum, None],
        quantity: Union[float, None],
        id: Optional[str] = None,
        compute_commission_rates: Optional[bool] = None,
        time_in_force: Optional[SorOrderTestTimeInForceEnum] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[SorOrderTestNewOrderRespTypeEnum] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[
            SorOrderTestSelfTradePreventionModeEnum
        ] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        sor_order_test(
            client=client,
            symbol=symbol,
            side=side,
            type=type,
            quantity=quantity,
            id=id,
            compute_commission_rates=compute_commission_rates,
            time_in_force=time_in_force,
            price=price,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,         
        )
    )


async def sor_order_place(
        client: Spot,
        symbol: Union[str, None],
        side: Union[SorOrderPlaceSideEnum, None],
        type: Union[SorOrderPlaceTypeEnum, None],
        quantity: Union[float, None],
        id: Optional[str] = None,
        time_in_force: Optional[SorOrderPlaceTimeInForceEnum] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[SorOrderPlaceNewOrderRespTypeEnum] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[SorOrderPlaceSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Places an order using smart order routing (SOR).
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.sor_order_place(
            symbol=symbol,
            side=side,
            type=type,
            quantity=quantity,
            id=id,
            time_in_force=time_in_force,
            price=price,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_sor_order_place(
        client: Spot,
        symbol: Union[str, None],
        side: Union[SorOrderPlaceSideEnum, None],
        type: Union[SorOrderPlaceTypeEnum, None],
        quantity: Union[float, None],
        id: Optional[str] = None,
        time_in_force: Optional[SorOrderPlaceTimeInForceEnum] = None,
        price: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[SorOrderPlaceNewOrderRespTypeEnum] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[SorOrderPlaceSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        sor_order_place(
            client=client,
            symbol=symbol,
            side=side,
            type=type,
            quantity=quantity,
            id=id,
            time_in_force=time_in_force,
            price=price,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,        
        )
    )


async def order_test(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderTestSideEnum, None],
        type: Union[OrderTestTypeEnum, None],
        id: Optional[str] = None,
        compute_commission_rates: Optional[bool] = None,
        time_in_force: Optional[OrderTestTimeInForceEnum] = None,
        price: Optional[float] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderTestNewOrderRespTypeEnum] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[OrderTestSelfTradePreventionModeEnum] = None,
        peg_price_type: Optional[OrderTestPegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderTestPegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Test order placement.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_test(
            symbol=symbol,
            side=side,
            type=type,
            id=id,
            compute_commission_rates=compute_commission_rates,
            time_in_force=time_in_force,
            price=price,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            peg_price_type=peg_price_type,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type,
            recv_window=recv_window,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_test(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderTestSideEnum, None],
        type: Union[OrderTestTypeEnum, None],
        id: Optional[str] = None,
        compute_commission_rates: Optional[bool] = None,
        time_in_force: Optional[OrderTestTimeInForceEnum] = None,
        price: Optional[float] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderTestNewOrderRespTypeEnum] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[OrderTestSelfTradePreventionModeEnum] = None,
        peg_price_type: Optional[OrderTestPegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderTestPegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_test(
            client=client,
            symbol=symbol,
            side=side,
            type=type,
            id=id,
            compute_commission_rates=compute_commission_rates,
            time_in_force=time_in_force,
            price=price,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            peg_price_type=peg_price_type,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type,
            recv_window=recv_window,      
        )
    )


async def order_place(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderPlaceSideEnum, None],
        type: Union[OrderPlaceTypeEnum, None],
        id: Optional[str] = None,
        time_in_force: Optional[OrderPlaceTimeInForceEnum] = None,
        price: Optional[float] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderPlaceNewOrderRespTypeEnum] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[OrderPlaceSelfTradePreventionModeEnum] = None,
        peg_price_type: Optional[OrderPlacePegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderPlacePegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Test order placement.
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_place(
            symbol=symbol,
            side=side,
            type=type,
            id=id,
            time_in_force=time_in_force,
            price=price,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            peg_price_type=peg_price_type,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type,
            recv_window=recv_window,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_place(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderPlaceSideEnum, None],
        type: Union[OrderPlaceTypeEnum, None],
        id: Optional[str] = None,
        time_in_force: Optional[OrderPlaceTimeInForceEnum] = None,
        price: Optional[float] = None,
        quantity: Optional[float] = None,
        quote_order_qty: Optional[float] = None,
        new_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderPlaceNewOrderRespTypeEnum] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        iceberg_qty: Optional[float] = None,
        strategy_id: Optional[int] = None,
        strategy_type: Optional[int] = None,
        self_trade_prevention_mode: Optional[OrderPlaceSelfTradePreventionModeEnum] = None,
        peg_price_type: Optional[OrderPlacePegPriceTypeEnum] = None,
        peg_offset_value: Optional[int] = None,
        peg_offset_type: Optional[OrderPlacePegOffsetTypeEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_place(
            client=client,
            symbol=symbol,
            side=side,
            type=type,
            id=id,
            time_in_force=time_in_force,
            price=price,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            new_client_order_id=new_client_order_id,
            new_order_resp_type=new_order_resp_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            iceberg_qty=iceberg_qty,
            strategy_id=strategy_id,
            strategy_type=strategy_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            peg_price_type=peg_price_type,
            peg_offset_value=peg_offset_value,
            peg_offset_type=peg_offset_type,
            recv_window=recv_window,    
        )
    )


async def order_list_place(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderListPlaceSideEnum, None],
        price: Union[float, None],
        quantity: Union[float, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        limit_client_order_id: Optional[str] = None,
        limit_iceberg_qty: Optional[float] = None,
        limit_strategy_id: Optional[int] = None,
        limit_strategy_type: Optional[int] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        stop_client_order_id: Optional[str] = None,
        stop_limit_price: Optional[float] = None,
        stop_limit_time_in_force: Optional[OrderListPlaceStopLimitTimeInForceEnum] = None,
        stop_iceberg_qty: Optional[float] = None,
        stop_strategy_id: Optional[int] = None,
        stop_strategy_type: Optional[int] = None,
        new_order_resp_type: Optional[OrderListPlaceNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListPlaceSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Send in a new one-cancels-the-other (OCO) pair:
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_list_place(
            symbol=symbol,
            side=side,
            price=price,
            quantity=quantity,
            id=id,
            list_client_order_id=list_client_order_id,
            limit_client_order_id=limit_client_order_id,
            limit_iceberg_qty=limit_iceberg_qty,
            limit_strategy_id=limit_strategy_id,
            limit_strategy_type=limit_strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            stop_client_order_id=stop_client_order_id,
            stop_limit_price=stop_limit_price,
            stop_limit_time_in_force=stop_limit_time_in_force,
            stop_iceberg_qty=stop_iceberg_qty,
            stop_strategy_id=stop_strategy_id,
            stop_strategy_type=stop_strategy_type,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_list_place(
        client: Spot,
        symbol: Union[str, None],
        side: Union[OrderListPlaceSideEnum, None],
        price: Union[float, None],
        quantity: Union[float, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        limit_client_order_id: Optional[str] = None,
        limit_iceberg_qty: Optional[float] = None,
        limit_strategy_id: Optional[int] = None,
        limit_strategy_type: Optional[int] = None,
        stop_price: Optional[float] = None,
        trailing_delta: Optional[int] = None,
        stop_client_order_id: Optional[str] = None,
        stop_limit_price: Optional[float] = None,
        stop_limit_time_in_force: Optional[OrderListPlaceStopLimitTimeInForceEnum] = None,
        stop_iceberg_qty: Optional[float] = None,
        stop_strategy_id: Optional[int] = None,
        stop_strategy_type: Optional[int] = None,
        new_order_resp_type: Optional[OrderListPlaceNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[OrderListPlaceSelfTradePreventionModeEnum] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_list_place(
            client=client,
            symbol=symbol,
            side=side,
            price=price,
            quantity=quantity,
            id=id,
            list_client_order_id=list_client_order_id,
            limit_client_order_id=limit_client_order_id,
            limit_iceberg_qty=limit_iceberg_qty,
            limit_strategy_id=limit_strategy_id,
            limit_strategy_type=limit_strategy_type,
            stop_price=stop_price,
            trailing_delta=trailing_delta,
            stop_client_order_id=stop_client_order_id,
            stop_limit_price=stop_limit_price,
            stop_limit_time_in_force=stop_limit_time_in_force,
            stop_iceberg_qty=stop_iceberg_qty,
            stop_strategy_id=stop_strategy_id,
            stop_strategy_type=stop_strategy_type,
            new_order_resp_type=new_order_resp_type,
            self_trade_prevention_mode=self_trade_prevention_mode,
            recv_window=recv_window,   
        )
    )


async def order_list_place_otoco(
        client: Spot,
        symbol: Union[str, None],
        working_type: Union[OrderListPlaceOtocoWorkingTypeEnum, None],
        working_side: Union[OrderListPlaceOtocoWorkingSideEnum, None],
        working_price: Union[float, None],
        working_quantity: Union[float, None],
        pending_side: Union[OrderListPlaceOtocoPendingSideEnum, None],
        pending_quantity: Union[float, None],
        pending_above_type: Union[OrderListPlaceOtocoPendingAboveTypeEnum, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderListPlaceOtocoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[
            OrderListPlaceOtocoSelfTradePreventionModeEnum] = None,
        working_client_order_id: Optional[str] = None,
        working_iceberg_qty: Optional[float] = None,
        working_time_in_force: Optional[OrderListPlaceOtocoWorkingTimeInForceEnum] = None,
        working_strategy_id: Optional[int] = None,
        working_strategy_type: Optional[int] = None,
        working_peg_price_type: Optional[OrderListPlaceOtocoWorkingPegPriceTypeEnum] = None,
        working_peg_offset_type: Optional[OrderListPlaceOtocoWorkingPegOffsetTypeEnum] = None,
        working_peg_offset_value: Optional[int] = None,
        pending_above_client_order_id: Optional[str] = None,
        pending_above_price: Optional[float] = None,
        pending_above_stop_price: Optional[float] = None,
        pending_above_trailing_delta: Optional[float] = None,
        pending_above_iceberg_qty: Optional[float] = None,
        pending_above_time_in_force: Optional[
            OrderListPlaceOtocoPendingAboveTimeInForceEnum] = None,
        pending_above_strategy_id: Optional[int] = None,
        pending_above_strategy_type: Optional[int] = None,
        pending_above_peg_price_type: Optional[
            OrderListPlaceOtocoPendingAbovePegPriceTypeEnum] = None,
        pending_above_peg_offset_type: Optional[
            OrderListPlaceOtocoPendingAbovePegOffsetTypeEnum] = None,
        pending_above_peg_offset_value: Optional[int] = None,
        pending_below_type: Optional[OrderListPlaceOtocoPendingBelowTypeEnum] = None,
        pending_below_client_order_id: Optional[str] = None,
        pending_below_price: Optional[float] = None,
        pending_below_stop_price: Optional[float] = None,
        pending_below_trailing_delta: Optional[float] = None,
        pending_below_iceberg_qty: Optional[float] = None,
        pending_below_time_in_force: Optional[
            OrderListPlaceOtocoPendingBelowTimeInForceEnum] = None,
        pending_below_strategy_id: Optional[int] = None,
        pending_below_strategy_type: Optional[int] = None,
        pending_below_peg_price_type: Optional[
            OrderListPlaceOtocoPendingBelowPegPriceTypeEnum] = None,
        pending_below_peg_offset_type: Optional[
            OrderListPlaceOtocoPendingBelowPegOffsetTypeEnum] = None,
        pending_below_peg_offset_value: Optional[int] = None,
        recv_window: Optional[int] = None,
    ) -> defaultdict:
    """
    Description:
        Send in a new one-cancels-the-other (OCO) pair:
    """
    connection = None
    try:
        connection = await client.websocket_api.create_connection()
        response = await connection.order_list_place_otoco(
            symbol=symbol,
            working_type=working_type,
            working_side=working_side,
            working_price=working_price,
            working_quantity=working_quantity,
            pending_side=pending_side,
            pending_quantity=pending_quantity,
            pending_above_type=pending_above_type,
            id=id,
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
            pending_below_type=pending_below_type,
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
            recv_window=recv_window,
            )
        return get_data(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            await connection.close_connection(close_session=True)


def call_order_list_place_otoco(
        client: Spot,
        symbol: Union[str, None],
        working_type: Union[OrderListPlaceOtocoWorkingTypeEnum, None],
        working_side: Union[OrderListPlaceOtocoWorkingSideEnum, None],
        working_price: Union[float, None],
        working_quantity: Union[float, None],
        pending_side: Union[OrderListPlaceOtocoPendingSideEnum, None],
        pending_quantity: Union[float, None],
        pending_above_type: Union[OrderListPlaceOtocoPendingAboveTypeEnum, None],
        id: Optional[str] = None,
        list_client_order_id: Optional[str] = None,
        new_order_resp_type: Optional[OrderListPlaceOtocoNewOrderRespTypeEnum] = None,
        self_trade_prevention_mode: Optional[
            OrderListPlaceOtocoSelfTradePreventionModeEnum] = None,
        working_client_order_id: Optional[str] = None,
        working_iceberg_qty: Optional[float] = None,
        working_time_in_force: Optional[OrderListPlaceOtocoWorkingTimeInForceEnum] = None,
        working_strategy_id: Optional[int] = None,
        working_strategy_type: Optional[int] = None,
        working_peg_price_type: Optional[OrderListPlaceOtocoWorkingPegPriceTypeEnum] = None,
        working_peg_offset_type: Optional[OrderListPlaceOtocoWorkingPegOffsetTypeEnum] = None,
        working_peg_offset_value: Optional[int] = None,
        pending_above_client_order_id: Optional[str] = None,
        pending_above_price: Optional[float] = None,
        pending_above_stop_price: Optional[float] = None,
        pending_above_trailing_delta: Optional[float] = None,
        pending_above_iceberg_qty: Optional[float] = None,
        pending_above_time_in_force: Optional[
            OrderListPlaceOtocoPendingAboveTimeInForceEnum] = None,
        pending_above_strategy_id: Optional[int] = None,
        pending_above_strategy_type: Optional[int] = None,
        pending_above_peg_price_type: Optional[
            OrderListPlaceOtocoPendingAbovePegPriceTypeEnum] = None,
        pending_above_peg_offset_type: Optional[
            OrderListPlaceOtocoPendingAbovePegOffsetTypeEnum] = None,
        pending_above_peg_offset_value: Optional[int] = None,
        pending_below_type: Optional[OrderListPlaceOtocoPendingBelowTypeEnum] = None,
        pending_below_client_order_id: Optional[str] = None,
        pending_below_price: Optional[float] = None,
        pending_below_stop_price: Optional[float] = None,
        pending_below_trailing_delta: Optional[float] = None,
        pending_below_iceberg_qty: Optional[float] = None,
        pending_below_time_in_force: Optional[
            OrderListPlaceOtocoPendingBelowTimeInForceEnum] = None,
        pending_below_strategy_id: Optional[int] = None,
        pending_below_strategy_type: Optional[int] = None,
        pending_below_peg_price_type: Optional[
            OrderListPlaceOtocoPendingBelowPegPriceTypeEnum] = None,
        pending_below_peg_offset_type: Optional[
            OrderListPlaceOtocoPendingBelowPegOffsetTypeEnum] = None,
        pending_below_peg_offset_value: Optional[int] = None,
        recv_window: Optional[int] = None,
    ):
    asyncio.run(
        order_list_place_otoco(
            client=client,
            symbol=symbol,
            working_type=working_type,
            working_side=working_side,
            working_price=working_price,
            working_quantity=working_quantity,
            pending_side=pending_side,
            pending_quantity=pending_quantity,
            pending_above_type=pending_above_type,
            id=id,
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
            pending_below_type=pending_below_type,
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
            recv_window=recv_window, 
        )
    )
