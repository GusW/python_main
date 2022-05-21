# Enter your code here. Read input from STDIN. Print output to STDOUT
"""


    1   2   3   4   5   6   7   8   9   10
    _____________________________________________________
ST1 42  E   14  14
ST2 E   E   28  60  78


"""

from typing import Any, Optional


class Stack:
    def __init__(self) -> None:
        self._items = []

    def get(self) -> Optional[Any]:
        return self._items[-1]

    def put(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        return self._items.pop()

    @property
    def is_empty(self) -> bool:
        return not self._items


class Queue:
    def __init__(self) -> None:
        self._stack1 = Stack()
        self._stack2 = Stack()

    def _transfer_stacks(self):
        if self._stack1.is_empty and not self._stack2.is_empty:
            while not self._stack2.is_empty:
                self._stack1.put(self._stack2.pop())

    def get(self) -> Optional[Any]:
        return self._stack1.get()

    def enqueue(self, item: Any) -> None:
        if self._stack1.is_empty:
            self._stack1.put(item)
        else:
            self._stack2.put(item)

    def dequeue(self) -> Optional[Any]:
        if self._stack1.get():
            self._stack1.pop()

        self._transfer_stacks()


if __name__ == "__main__":

    t = int(input().strip())
    q = Queue()
    for t_itr in range(t):
        s = input()
        if s[0] == "1":
            val = s.split(" ")[1]
            q.enqueue(val)
        elif s[0] == "2":
            q.dequeue()
        elif s[0] == "3":
            print(q.get())
