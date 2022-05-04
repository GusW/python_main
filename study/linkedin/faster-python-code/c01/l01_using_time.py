"""Measuring time"""

from time import perf_counter
from typing import Callable


def measure_time(function: Callable) -> Callable:
    def _measure_time(*args, **kwargs) -> None:
        start = perf_counter()
        function(*args, **kwargs)
        duration = perf_counter() - start
        print(function.__name__, duration, "sec")

    return _measure_time


@measure_time
def upto_for(n) -> int:
    """Sum 1...n with a for loop"""
    total = 0
    for i in range(n):
        total += i
    return total


@measure_time
def upto_sum(n) -> int:
    """Sum 1...n with built-in sum and range"""
    return sum(range(n))


if __name__ == "__main__":
    n = 1_000_000
    upto_for(n)
    upto_sum(n)
