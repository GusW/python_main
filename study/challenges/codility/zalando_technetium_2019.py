"""
https://app.codility.com/programmers/challenges/technetium2019/s
You are given a matrix A consisting of N rows and M columns, where each cell contains a digit. Your task is to find a continuous sequence of neighbouring cells, starting in the top-left corner and ending in the bottom-right corner (going only down and right), that creates the biggest possible integer by concatenation of digits on the path. By neighbouring cells we mean cells that have exactly one common side.

Write a function:

def solution(A)

that, given matrix A consisting of N rows and M columns, returns a string which represents the sequence of cells that we should pick to obtain the biggest possible integer.

For example, given the following matrix A:

[9 9 7]
[9 7 2]
[6 9 5]
[9 1 2]

the function should return "997952", because you can obtain such a sequence by choosing a path as shown below:

[9 9 *]
[* 7 *]
[* 9 5]
[* * 2]

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000];
each element of matrix A is an integer within the range [1..9].
"""


def solution(a):
    from queue import Queue

    def get_current_item(row, column):
        return a[row][column]

    def concat_visited_items(current_string, new_int):
        return ''.join([current_string, str(new_int)])

    q = Queue()
    row = column = 0
    max_column = len(a[0]) - 1
    max_row = len(a) - 1
    curr_item = get_current_item(row, column)
    max_observed_item = str(curr_item)
    q.put((str(curr_item), row, column))
    while not q.empty():
        item, row, column = q.get()
        target_row_item = target_column_item = '0'
        target_row, target_column = row, column
        if row < max_row:
            target_row += 1
            target_row_item = concat_visited_items(item, get_current_item(target_row, column))

        if column < max_column:
            target_column += 1
            target_column_item = concat_visited_items(item, get_current_item(row, target_column))

        if target_row_item >= target_column_item:
            q.put((target_row_item, target_row, column))

        if target_column_item > target_row_item:
            q.put((target_column_item, row, target_column))

        target_item = target_row_item if target_row_item >= target_column_item else target_column_item
        max_observed_item = target_item if target_item > max_observed_item else max_observed_item

        if row == max_row and column == max_column:
            print(max_observed_item)  # just for debugging purposes
            return max_observed_item


def main():
    test_ex = [[9, 9, 7],
               [9, 7, 2],
               [6, 9, 5],
               [9, 1, 2]]

    # test_ex = [[3,1,1]]

    return solution(test_ex)


if __name__ == "__main__":
    main()
