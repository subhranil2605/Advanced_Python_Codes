import logging
from functools import wraps
from typing import Callable, Any


logging.basicConfig(level=logging.INFO)


def log_function(func: Callable) -> Callable:

    @wraps(func)
    def wrapper_log_function(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Calling function: {func.__name__}")
        logging.info(f"Arguments: {args}, {kwargs}")
        result: Any = func(*args, **kwargs)
        logging.info(f"Result: {result}")
        return result

    return wrapper_log_function


@log_function
def add_numbers(x: int, y: int) -> int:
    """
    Add two integers
    """
    return x + y


print(add_numbers(5, 6))
