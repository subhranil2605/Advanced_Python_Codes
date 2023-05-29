

def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> int:
    assert y != 0, "Cannot divide by zero!"
    return x / y


if __name__ == "__main__":
    print(divide(10, 0))
