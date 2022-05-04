from l01_fib import fib, lru_fib


def test_fib(benchmark):
    if 0:
        result = benchmark(fib, 30)
        assert result == 1346269

    if 1:
        result = benchmark(lru_fib, 30)
        assert result == 1346269
