'''
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
'''
import os


def _validate_constrains(a, d):
    return (1 <= d <= len(a)
            and 1 <= min(a)
            and max(a) <= 10**6)


def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
