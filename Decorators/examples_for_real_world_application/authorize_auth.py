from functools import wraps
from typing import Callable, Any


# Simulated authentication function
def authenticate(username: str, password: str) -> bool:
    return username == "admin" and password == "12345"


# Authorization decorator
def authorize(username: str, password: str) -> Callable:
    def auth_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper_authorize(*args: Any, **kwargs: Any):
            # Check if user is authenticated
            if authenticate(username, password):
                return func(*args, **kwargs)
            else:
                raise PermissionError("Unauthorized access!")

        return wrapper_authorize

    return auth_decorator


username: str = "admin"
password: str = "12345"


# Example function to be decorated
@authorize(username, password)
def sensitive_operation():
    print("Performing sensitive operation")


sensitive_operation()
