#!/usr/bin/python3
from datetime import datetime


def timeit(fn):
    def decorated(*args, **kwargs):
        init = datetime.now()
        x = fn(*args, **kwargs)
        end = datetime.now()
        print(f'Time elapsed => {end - init}')

        return x

    return decorated


@timeit
def fibonacci_bottom_up(n):
    if n == 1 or n == 2:
        return 1

    memo = [None] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    curr = 3
    while curr <= n + 1:
        if memo[n]:
            return memo[n]

        memo[curr] = memo[curr-1] + memo[curr-2]
        curr += 1


@timeit
def factorial_bottom_up(n):
    if n == 1:
        return 1
    res = [None] * (n + 1)
    res[1] = 1
    curr = 2
    while curr <= n + 1:
        if res[n]:
            return res[n]

        res[curr] = res[curr - 1] * curr
        curr += 1


def findPossibleMoves(mat, p, q):
    m = n = 4  # board size

    # All possible moves of a knight
    X = [2, 1, -1, -2, -2, -1, 1, 2]
    Y = [1, 2, 2, 1, -1, -2, -2, -1]

    count = 0

    for X, Y in zip(X, Y):
        x = p + X
        y = q + Y

        if(x >= 0 and y >= 0 and x < n and y < m and mat[x][y] == 0):  # 0 == empty space
            count += 1

    return count


@timeit
def fibonacci_generator(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


@timeit
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        yield res


def main():
    from collections import deque
    # *_, last = fibonacci_generator(60000)
    # print(last)

    # fib = fibonacci_bottom_up(60000)
    # print(fib)

    fac = factorial(1000)
    dd = deque(fac, maxlen=1)
    print(dd.pop())

    print(factorial_bottom_up(1000))

    mat = [[1, 0, 1, 0],
           [0, 1, 1, 1],
           [1, 1, 0, 1],
           [0, 1, 1, 1]]
    p = q = 2
    print(findPossibleMoves(mat, p, q))


if __name__ == '__main__':
    main()
