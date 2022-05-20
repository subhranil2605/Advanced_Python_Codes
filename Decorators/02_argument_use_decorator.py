# Python Decorators with the use of args in the function


def func(fun):
    def wrapper(*args, **kwargs):
        print("Starting")
        fun(*args, **kwargs)
        print("End")

    return wrapper


@func
def f(name):
    print(f"Hello, {name}")


# calling the function
f("Subhranil Sarkar")
