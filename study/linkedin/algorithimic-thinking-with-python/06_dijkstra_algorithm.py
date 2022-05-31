from math import inf
from collections import OrderedDict
import heapq


def dijkstra(graph):
    visited = set()
    unvisited = list(graph.keys())
    vertex_map = {k: inf for k in unvisited}
    heap = []

    def _handle_curr_item(item):
        priority, item_ = item

        visited.add(item_)

        if item_ in unvisited:
            unvisited.remove(item_)

        for key, val in graph.get(item_).items():
            diff_from_start = priority + val
            if diff_from_start < vertex_map[key]:
                vertex_map[key] = diff_from_start
                if key not in visited:
                    heapq.heappush(heap, (diff_from_start, key))

    first = unvisited.pop(0)
    priority = 0
    vertex_map[first] = priority
    _handle_curr_item((priority, first))

    while unvisited:
        curr_item = heapq.heappop(heap)
        _handle_curr_item(curr_item)

    return vertex_map


if __name__ == "__main__":
    d1 = OrderedDict()
    d1["U"] = {"V": 6, "W": 7}
    d1["V"] = {"U": 6, "X": 10}
    d1["W"] = {"U": 7, "X": 1}
    d1["X"] = {"W": 1, "V": 10}
    print(dijkstra(d1))
    # [('U', 0), ('V', 6), ('W', 7), ('X', 8)]

    d2 = OrderedDict()
    d2["A"] = {"B": 6, "D": 1}
    d2["B"] = {"A": 6, "C": 5, "D": 2, "E": 2}
    d2["C"] = {"B": 5, "E": 5}
    d2["D"] = {"A": 1, "B": 2, "E": 1}
    d2["E"] = {"B": 2, "C": 5, "D": 1}
    print(dijkstra(d2))
    # [('A', 0), ('B', 3), ('C', 7), ('D', 1), ('E', 2)]
