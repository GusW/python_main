#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat """
# if we simulate a CPU bound operation (cpu_work) then processes are presumably better than threads
# Also, the Python GIL won´t allow mutiple threads running in parallel
import multiprocessing as mp

serving_line = mp.Queue(5)

consumer_amount = 2


def cpu_work(work_units):
    x = 0
    for _ in range(work_units * 1_000_000):
        x += 1


def soup_producer(serving_line):
    for i in range(20):  # serve 20 bowls of soup
        serving_line.put_nowait("Bowl #" + str(i))
        print(
            "Served Bowl #",
            str(i),
            "- remaining capacity:",
            serving_line._maxsize - serving_line.qsize(),
        )
        cpu_work(3)  # time to serve a bowl of soup

    for _ in range(consumer_amount):
        serving_line.put_nowait("no soup for you!")


def soup_consumer(serving_line):
    while True:
        bowl = serving_line.get()
        if bowl == "no soup for you!":
            break
        print("Ate", bowl)
        cpu_work(4)  # time to eat a bowl of soup


if __name__ == "__main__":
    for _ in range(consumer_amount):
        mp.Process(target=soup_consumer, args=(serving_line,)).start()

    mp.Process(target=soup_producer, args=(serving_line,)).start()
