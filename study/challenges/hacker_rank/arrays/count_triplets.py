#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr) < 3:
        return 0

    ratio_target = [1, r, r*r]

    all_subsets = combinations(arr, 3)
    counts = Counter(all_subsets)
    counter = 0
    for subset, count in counts.items():
        if len(set([s/r for s, r in zip(subset, ratio_target)])) == 1:
            counter += count

    return counter
"""
    0   1   2
    -   -   -
    1   2   4
    -   -   -
    i   ii  iii

    ratio_target = [1,2,4]



    0   1   2   3
    -   -   -   -
    1   2   2   4
    -   -   -   -
    i   ii      iii
    i       ii  iii
    -   -   -   -

    ratio_target = [1,2,4]


R = 2



    0   1   2   3   4   5
    -   -   -   -   -   -
    1   3   9   9   27  81
    -   -   -   -   -   -
    i   ii  iii
    i   ii      iii
        i   ii      iii
        i       ii  iii
            i       ii  iii
                i   ii  iii
    -   -   -   -   -   -
R = 6
"""


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
