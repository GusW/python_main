from time import perf_counter, sleep


def _sync_sec(seconds) -> None:
    print(f'dummy sleep {seconds}s')
    sleep(seconds)


if __name__ == "__main__":
    time_init = perf_counter()
    for _ in range(100):
        _sync_sec(2.5)

    print(f'Time elapsed => {round(perf_counter()-time_init, 2)}s')
