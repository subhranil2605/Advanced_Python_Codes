from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


def get_item(key: K, container: dict[K, V]) -> V:
    return container.get(key)


def get_first(container: dict[K, V]) -> K:
    return list(container.keys())[0]


if __name__ == '__main__':
    test: dict[str, int] = {"k": 1}
    print(get_item('k', test))
    print(get_first(container=test))
