from typing import Optional, Any


class Stack:
    def __init__(self) -> None:
        self._items = []

    def is_empty(self) -> bool:
        return not self._items

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        return self._items.pop()

    def peek(self) -> Optional[Any]:
        return self._items[-1]

    def size(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __repr__(self) -> str:
        return str(self._items)


if __name__ == "__main__":
    stack = Stack()
    print(f"stack: {stack}")

    print(f"stack.is_empty(): {stack.is_empty()}")

    stack.push(3)
    print(f"stack: {stack}")

    stack.push(7)
    stack.push(5)
    print(f"stack: {stack}")

    print(f"stack.pop(): {stack.pop()}")
    print(f"stack: {stack}")

    print(f"stack.peek(): {stack.peek()}")
    print(f"stack.size(): {stack.size()}")
