#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat """
# time does not impact in CPU usage so it could be faced as I/O bound
# for I/O bound operations, the Python GIL isn't a major issue => threading
import queue
import threading
import time

serving_line = queue.Queue(maxsize=5)


def soup_producer():
    for i in range(20):  # serve 20 bowls of soup
        serving_line.put_nowait("Bowl #" + str(i))
        print(
            "Served Bowl #",
            i,
            "- remaining capacity:",
            serving_line.maxsize - serving_line.qsize(),
        )
        time.sleep(0.2)  # time to serve a bowl of soup
    serving_line.put_nowait("no soup for you!")
    serving_line.put_nowait("no soup for you!")


def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == "no soup for you!":
            break
        print("Ate", bowl)
        time.sleep(0.3)  # time to eat a bowl of soup


if __name__ == "__main__":
    for consumer in range(2):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
