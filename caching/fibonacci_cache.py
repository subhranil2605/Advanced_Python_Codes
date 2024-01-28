from time import perf_counter
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

if __name__ == '__main__':
    start_time = perf_counter()
    result = fibonacci(200)
    run_time = perf_counter() - start_time
    print(f"Result = {result} and time: {run_time:.6f} seconds")
