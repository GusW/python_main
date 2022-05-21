#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    def _print_decimals(float_number: float):
        print(f'{float_number:.6f}')

    counters = {"positive": 0, "negative": 0, "zero": 0}
    for number in arr:
        if number > 0:
            counters["positive"] += 1
        elif number < 0:
            counters["negative"] += 1
        else:
            counters["zero"] += 1

    arr_len = len(arr)
    _print_decimals(counters["positive"]/arr_len)
    _print_decimals(counters["negative"]/arr_len)
    _print_decimals(counters["zero"]/arr_len)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
