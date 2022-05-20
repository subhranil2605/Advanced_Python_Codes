'''
decorators should use the @functools.wraps decorator,
which will preserve information about the original function
'''

import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hello, {name}"


print(return_greeting("Roni"))
