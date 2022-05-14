'''
https://www.hackerrank.com/challenges/crush/problem
'''
import os
from collections import deque


def arrayManipulation(n, queries):
    current_array = [0 for _ in range(n+1)]
    for q in queries:
        a, b, k = q
        a -= 1
        current_array[a] += k
        current_array[b] -= k

    curr_val = max_val = 0
    for val in current_array:
        curr_val += val
        max_val = curr_val if curr_val > max_val else max_val

    return max_val


if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    queries = deque()

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
