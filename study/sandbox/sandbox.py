from collections import deque


def _transpose_arr_to_match_programming_index(arr):
    return deque(list(map(lambda x: x-1, arr)))


def _swap_item(transposed_arr, item, ix):
    current_ix = transposed_arr.index(ix)
    transposed_arr[ix], transposed_arr[current_ix] = ix, item
    return transposed_arr


def minimumSwaps(arr):
    transposed_arr = _transpose_arr_to_match_programming_index(arr)
    total_count = 0
    for ix in range(len(transposed_arr)-1):
        # print(f'transposed_arr == {transposed_arr}')
        item = transposed_arr[ix]
        # print(f'ix:item == {ix}:{item}')
        if item != ix:
            total_count += 1
            transposed_arr = _swap_item(transposed_arr, item, ix)

    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
