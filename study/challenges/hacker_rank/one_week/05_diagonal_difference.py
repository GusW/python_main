#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""
[11,2,4],
[4,5,6],
[10,8,-12],
"""


def diagonalDifference(arr):
    diag_total_1, diag_total_2 = 0, 0
    for idx, row in enumerate(arr):
        diag_total_1 += row[idx]
        diag_total_2 += row[-1+(-1*(idx))]

    return abs(diag_total_1 - diag_total_2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
