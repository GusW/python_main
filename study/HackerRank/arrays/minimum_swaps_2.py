'''
https://www.hackerrank.com/challenges/minimum-swaps-2/problem
'''
import os
from collections import deque


def _transpose_arr_to_match_programming_index(arr):
    return deque(list(map(lambda x: x-1, arr)))


def _swap_item(transposed_arr, ref_array_map, item, ix):
    current_ix = ref_array_map.get(ix)

    transposed_arr[ix], transposed_arr[current_ix] = ix, item
    ref_array_map[ix], ref_array_map[item] = ix, current_ix

    return transposed_arr, ref_array_map


def _ref_array_map(arr):
    return {item: ix for ix, item in enumerate(arr)}


def minimumSwaps(arr):
    transposed_arr = _transpose_arr_to_match_programming_index(arr)
    ref_array_map = _ref_array_map(transposed_arr)
    total_count = 0
    for ix in range(len(transposed_arr)-1):
        item = transposed_arr[ix]
        if item != ix:
            total_count += 1
            transposed_arr, ref_array_map = _swap_item(transposed_arr,
                                                       ref_array_map,
                                                       item,
                                                       ix)

    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
