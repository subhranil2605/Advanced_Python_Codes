from functools import reduce


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers = [0, 1, 2, 5, 9]

print(reduce(my_add, numbers, 100))
