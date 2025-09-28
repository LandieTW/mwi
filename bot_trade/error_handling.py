
from binance_common.errors import (
    ClientError,
    UnauthorizedError,
    ForbiddenError,
    TooManyRequestsError,
    RequiredError,
    RateLimitBanError,
    ServerError,
    NetworkError,
    NotFoundError,
    BadRequestError
)

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ClientError as e:
            print("Client error: Check your request parameters.", e)
            return None
        except RequiredError as e:
            print("Missing required parameters.", e)
            return None
        except UnauthorizedError as e:
            print("Unauthorized: Invalid API credentials.", e)
            return None
        except ForbiddenError as e:
            print("Forbidden: Check your API key permissions.", e)
            return None
        except TooManyRequestsError as e:
            print("Rate limit exceeded. Please wait and try again.", e)
            return None
        except RateLimitBanError as e:
            print("IP address banned due to excessive rate limits.", e)
            return None
        except ServerError as e:
            print("Server error: Try again later.", e)
            return None
        except NetworkError as e:
            print("Network error: Check your internet connection.", e)
            return None
        except NotFoundError as e:
            print("Resource not found.", e)
            return None
        except BadRequestError as e:
            print("Bad request: Verify your input parameters.", e)
            return None
        except Exception as e:
            print("An unexpected error occurred:", e)
            return None
    return wrapper
