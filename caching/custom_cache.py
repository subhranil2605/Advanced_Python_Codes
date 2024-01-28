from time import perf_counter
from functools import lru_cache


@lru_cache(maxsize=None)
def power(base, exponent):
    return base ** exponent


if __name__ == '__main__':
    # Manually evict a specific cache entry
    power.cache_clear()
    print(power(2, 3))     # This will cache the result for (2, 3)
    power.cache_clear()
    print(power(2, 3))     # This will recompute the result since the cache was clear