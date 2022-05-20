import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something here
        value = func(*args, **kwargs)
        # Do something here
        return value

    return wrapper_decorator
