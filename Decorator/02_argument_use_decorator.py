# Python Decorator with the use of args in the function


def func(func):
    def wrapper(*args, **kwargs):
        print("Starting")
        func(*args, **kwargs)
        print("End")
    return wrapper


@func
def f(name):
    print(f"Hello, {name}")


# calling the function
f("Subhranil Sarkar")


