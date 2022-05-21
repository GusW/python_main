#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):

    arr_len = len(arr)
    arr_idx = arr.index

    min_el = min(arr)
    first_min_el_idx = arr_idx(min_el, 0)
    max_sum = sum([*arr[0:first_min_el_idx], *arr[first_min_el_idx+1:arr_len]])

    max_el = max(arr)
    first_max_el_idx = arr_idx(max_el, 0)
    min_sum = sum([*arr[0:first_max_el_idx], *arr[first_max_el_idx+1:arr_len]])
    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
