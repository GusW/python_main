import heapq
from typing import Any, Optional


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self) -> bool:
        return not self.elements

    def put(self, item: Any, priority: int) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Optional[Any]:
        # [1] = item, from tuple (priority, item)
        return heapq.heappop(self.elements)[1]

    def __str__(self) -> str:
        return str(self.elements)

    def __repr__(self) -> str:
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)

    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())

    print(pq)
