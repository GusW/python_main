from typing import Any, Optional


def solution1(arr: list[Any], target: Any) -> Optional[list[int]]:
    head_idx = 0
    tail_idx = len(arr) - 1
    start_idx, end_idx = None, None
    while (head_idx < len(arr) and tail_idx > 0):
        if not start_idx:
            if arr[head_idx] == target:
                start_idx = head_idx
            else:
                head_idx += 1

        if not end_idx:
            if arr[tail_idx] == target:
                end_idx = tail_idx
            else:
                tail_idx -= 1

        if start_idx and end_idx:
            return [start_idx, end_idx]

    return [-1, -1]


# TODO implement with binary search
def solution2():
    pass


if __name__ == '__main__':
    array1 = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 5
    print(solution1(array1, target))

    array2 = [7, 2, 5, 4, 3, 1, 7, 6]
    print(solution1(array2, target))

    array3 = [7, 2, 5, 4, 3, 1, 7, 6]
    print(solution1(array2, 9))
