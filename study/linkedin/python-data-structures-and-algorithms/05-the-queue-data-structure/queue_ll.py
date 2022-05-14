from collections import deque
from typing import Any, Optional


class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Optional[Any]:
        return self.items.popleft()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Optional[Any]:
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)

    def __repr__(self) -> str:
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    print(f"queue: {queue}")
    print(f"queue.is_empty(): {queue.is_empty()}")

    queue.enqueue("A")
    queue.enqueue("D")
    queue.enqueue("F")
    print(f"queue: {queue}")

    print(f"queue.dequeue(): {queue.dequeue()}")
    print(f"queue.dequeue(): {queue.dequeue()}")
    print(f"queue: {queue}")

    print(f"queue.size(): {queue.size()}")

    print(f"queue.peek(): {queue.peek()}")

    print(f"queue: {queue}")
