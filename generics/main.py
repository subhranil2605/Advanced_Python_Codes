from typing import TypeVar

T = TypeVar("T")


def first(container: list[T]) -> T:
    return container[0]


if __name__ == '__main__':
    list_one: list[str] = ["a", "b", "c"]
    print(first(list_one))

    list_two: list[int] = [1, 2, 3]
    print(first(list_two))
