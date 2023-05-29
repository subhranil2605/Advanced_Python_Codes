from functools import wraps
from typing import Callable, Any
import re


def is_valid_email(email: str):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_password(password) -> tuple[bool, str]:
    # Check if password meets the required criteria
    # return (
    #     len(password) >= 6
    #     and re.search(r"[A-Z]", password)       # one uppercase
    #     and re.search(r"[a-z]", password)       # one lowercase
    #     and re.search(r"\d", password)          # one digit
    #     and re.search(r"[@#$%^&+=]", password)  # one symbol
    # )

    # Check if password meets the required criteria
    if len(password) < 6:
        mssg = "Password length must be 6 characters"
        return False, mssg

    if not re.search(r"[A-Z]", password):  # Check for at least one uppercase letter
        mssg = "Missing at least one uppercase letter"
        return False, mssg

    if not re.search(r"[a-z]", password):  # Check for at least one lowercase letter
        mssg = "Missing at least one lowercase letter"
        return False, mssg

    if not re.search(r"\d", password):  # Check for at least one digit
        mssg = "Missing at least one digit"
        return False, mssg

    if not re.search(r"[@#$%^&+=]", password):  # Check for at least one symbol
        mssg = "Missing at least one symbol (@#$%^&+=)"
        return False, mssg

    return True, "success"


# Input validation decorator
def validate_input(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(email, password, *args, **kwargs):
        # Perform input validation

        if not is_valid_email(email):
            raise ValueError("Invalid email format")
        
        valid_password, mssg = is_valid_password(password)

        if not valid_password:
            raise ValueError(mssg)

        # if not all(isinstance(arg, int) for arg in args):
        #     raise ValueError("Invalid input: Args should be integers")

        # if not all(isinstance(value, str) for value in kwargs.values()):
        #     raise ValueError("Invalid input: Kwargs should be str")

        return func(email, password, *args, **kwargs)

    return wrapper


@validate_input
def register_user(email, password):
    print("User registration successful")


register_user("hello@example.com", "12345@DevaDeva")
register_user("hello@example.com", "12345@Devadeva")
