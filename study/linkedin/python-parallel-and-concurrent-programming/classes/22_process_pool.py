#!/usr/bin/env python3
""" Chopping vegetables with a ThreadPool """


from concurrent.futures import ProcessPoolExecutor
import os


def cpu_bound_work():
    x = 0
    for _ in range(1_000_000):
        x += 1


def vegetable_chopper(vegetable_id):
    name = os.getpid()
    print(name, "chopped a vegetable", vegetable_id)
    cpu_bound_work()


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as pool:
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)
