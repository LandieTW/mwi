
from typing import List
from typing import Optional

from collections import defaultdict

from binance_sdk_spot.spot import Spot
from binance_common.models import ApiResponse
from binance_sdk_spot.rest_api.models import ExchangeInfoSymbolStatusEnum

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



