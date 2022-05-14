from collections import Counter
from typing import Iterable


"""_summary_
"""


def solution(iterableA: Iterable[any], iterableB: Iterable[any]) -> bool:
    return Counter(iterableA) == Counter(iterableB) if len(iterableA) == len(iterableB) else False


def solution_(iterableA: Iterable[any], iterableB: Iterable[any]) -> bool:
    return sorted(iterableA) == sorted(iterableB) if len(iterableA) == len(iterableB) else False


if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5, 6, 7, 7]
    array2 = [7, 2, 5, 4, 3, 1, 7, 6]
    print('array1 <-> array2: ', solution(array1, array2))
    print('array1 <-> array2: ', solution_(array1, array2))

    array3 = [7, 2, 4, 3, 1, 7, 6]
    print('array1 <-> array3: ', solution(array1, array3))
    print('array1 <-> array3: ', solution_(array1, array3))
