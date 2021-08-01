import multiprocessing
from time import perf_counter, sleep


def _sync_sec(seconds: float) -> None:
    print(f'dummy sleep {seconds}s')
    sleep(seconds)


def _trigger_multiprocessing_for_fn(fn, *args):
    # create individual processes
    p = multiprocessing.Process(target=fn, args=args)
    # start processes
    p.start()
    return p


if __name__ == "__main__":
    time_init = perf_counter()

    processes = [_trigger_multiprocessing_for_fn(_sync_sec, 2.5) for _ in range(100)]
    # processes must be joined to finish before moving foward on code
    list(map(lambda x: x.join(), processes))

    print(f'Time elapsed => {round(perf_counter()-time_init, 2)}s')
