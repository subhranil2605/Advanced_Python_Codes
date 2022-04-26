# decorator using returning the value of the function


def func(fun):
    def wrapper(*args, **kwargs):
        print("Starting...")
        val = fun(*args, **kwargs)
        print("Ending...")
        return val

    return wrapper


@func
def add(x, y):
    return x + y


# stroing the return value in a new variable
result = add(5, 6)

print(result)
