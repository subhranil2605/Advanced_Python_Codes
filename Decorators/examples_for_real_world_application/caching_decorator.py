from functools import wraps
from typing import Callable, Any

from timer_decorator import timer


def cache(func):
    # dictionary to store cached results
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            # return cached result if available
            print(f"Returning cached result for {args}")
            return cache_dict[args]

        result = func(*args)

        cache_dict[args] = result

        # print("Caching result for", args)

        return result

    return wrapper


# @cache
def compute_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * compute_factorial(n - 1) 


@timer
def main(value):
    return compute_factorial(value)


print(main(300))