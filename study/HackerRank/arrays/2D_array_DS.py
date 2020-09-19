'''
https://www.hackerrank.com/challenges/2d-array/problem
'''
import os

from collections import deque


def _get_sublist_lenght(arr):
    return list(set([len(sublist) for sublist in arr]))[0]


def _validate_constrains(arr):
    flatten_list = [item for sublist in arr for item in sublist]
    return (1 <= len(arr) <= 6
            and 1 <= _get_sublist_lenght(arr) <= 6
            and max(flatten_list) <= 9
            and min(flatten_list) >= -9)


def _get_hourglass_elements_sum(arr, target_row, target_column):
    first_el = arr[target_row][target_column]
    second_el = arr[target_row][target_column + 1]
    third_el = arr[target_row][target_column + 2]
    forth_el = arr[target_row + 1][target_column + 1]
    fifth_el = arr[target_row + 2][target_column]
    sixth_el = arr[target_row + 2][target_column + 1]
    seventh_el = arr[target_row + 2][target_column + 2]
    return (first_el +
            second_el +
            third_el +
            forth_el +
            fifth_el +
            sixth_el +
            seventh_el)


def hourglassSum(arr):
    if _validate_constrains(arr):
        hourglass_el_sum = deque()
        row_boundary = len(arr) - 2
        col_boundary = _get_sublist_lenght(arr) - 2
        for i in range(row_boundary):
            for j in range(col_boundary):
                hourglass_el_sum.append(_get_hourglass_elements_sum(arr, i, j))

        return max(hourglass_el_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
