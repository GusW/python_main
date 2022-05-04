"""Simple fibonacci"""

from functools import lru_cache


def fib(n):
    """Return n'th fibonacci number"""
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


@lru_cache()
def lru_fib(n):
    """Return n'th fibonacci number"""
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
