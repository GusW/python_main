# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
empty string S
perform Q operations
1. append
2. delete
3. print
4. undo
"""


class EditorString:
    def __init__(self) -> None:
        self._string = ""
        self.history = []

    def print_(self, idx: str) -> str:
        print(self._string[int(idx)-1])

    def append(self, chars: str) -> None:
        self.history.append(self._string)
        self._string += chars

    def delete(self, amount: str) -> None:
        self.history.append(self._string)
        self._string = self._string[:-(int(amount))]

    def undo(self) -> str:
        self._string = self.history.pop()


editor = EditorString()

_INT_TO_METHOD_MAP = {
    1: lambda W: editor.append(W),
    2: lambda k: editor.delete(k),
    3: lambda k: editor.print_(k),
    4: lambda: editor.undo(),
}


def process_editor_commands(op, param) -> str:
    target_fn = _INT_TO_METHOD_MAP.get(int(op))
    return target_fn(param) if param else target_fn()


if __name__ == "__main__":
    ops_amount_Q = int(input().strip())
    while ops_amount_Q > 0:
        commands = input().strip()
        op = int(commands[0])
        param = None
        if op in [1, 2, 3]:
            param = commands[1:].replace(" ", "")

        process_editor_commands(op, param)
        ops_amount_Q -= 1
