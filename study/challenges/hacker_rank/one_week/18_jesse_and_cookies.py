#!/bin/python3

import os
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

"""
Amount of iterations needed until all array items are >= k
Process:
0. counter = 0
1. Identify the min value                   = min_val
2. Identify the 2nd min value               = next_min_val
3. Pop min_val and next_min_val from array
4. Calculate: min_val + next_min_val * 2    = new_val
5. Append new_val to array
6. Increment iteration counter
7. Repeat process until all items are >= given k
8?. If it's not possible return -1?

ex.: 1 2 3 9 10 12


1. min_val = 1
2. next_min_val = 2
3. arr = [3, 9, 10, 12]
4. new_val = 5
5. arr = [3, 5, 9, 10, 12]
6. counter += 1
7. recurse
"""


def _cookies(k, A, counter=0):
    while True:
        min_val = heapq.heappop(A)
        if min_val >= k:
            return counter

        if len(A) == 0:
            return -1

        heapq.heappush(A, min_val + heapq.heappop(A) * 2)
        counter += 1


def cookies(k, A):
    heapq.heapify(A)
    return _cookies(k, A)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
