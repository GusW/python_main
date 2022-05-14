import concurrent.futures
from time import perf_counter, sleep


def _sync_sec(seconds: float) -> None:
    sleep(seconds)
    return f'dummy sleep {seconds}s'


if __name__ == "__main__":
    time_init = perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # submit returns future objects
        results = [executor.submit(_sync_sec, 2.5) for _ in range(100)]
        # need to call as_completed to return from the futures
        list(map(lambda x: print(x.result()),
             concurrent.futures.as_completed(results)))

    print(
        f'Time elapsed with submit/as_completed => {round(perf_counter()-time_init, 2)}s')

    # OR
    time_init = perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        items = [2.5] * 100
        # executor map will submit and return to a whole iterable
        results = executor.map(_sync_sec, items)
        list(map(print, results))

    print(f'Time elapsed with map => {round(perf_counter()-time_init, 2)}s')
