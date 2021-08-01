import threading
from time import perf_counter, sleep


def _sync_sec(seconds: float) -> None:
    print(f'dummy sleep {seconds}s')
    sleep(seconds)


def _trigger_threading_for_fn(fn, *args):
    # create individual thread
    t = threading.Thread(target=fn, args=args)
    # start thread
    t.start()
    return t


if __name__ == "__main__":
    time_init = perf_counter()

    threads = [_trigger_threading_for_fn(_sync_sec, 2.5) for _ in range(100)]
    # threads must be joined to finish before moving foward on code
    list(map(lambda x: x.join(), threads))

    print(f'Time elapsed => {round(perf_counter()-time_init, 2)}s')
