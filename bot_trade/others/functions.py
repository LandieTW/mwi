
from binance_common.models import ApiResponse
from collections import defaultdict

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