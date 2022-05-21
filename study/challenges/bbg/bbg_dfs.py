desert = [                             # 0 1 2 3
    ['.', '.', '.', 'o'],          # 0            O
    ['.', '3', '.', '.'],          # 1        R
    ['.', '*', '*', '.'],          # 2        x
    ['.', 'c', '.', '.']           # 3      x C x
]

#   9  8  7  6  5  3  2  1  0
# [ 9, ., ., ., C, ., ., ., ., O]


"""
car = 3,1
end = 0,3
fuel= 1,1

row_offset_end = 3-0 = 3
col_offset_end = 3-1 = 2 if was 0 then

row_offset_fuel = 2
col_offset_fuel = 0

3,1
(2,1)


{
    3,1: 4
    3,2: 3
    3,0: 3
    2,0: 2
    1,0: 1

}


"""

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def _parse_car_idxs_to_str(row_idx: int, col_idx: int):
    return ','.join(map(str, [row_idx, col_idx]))


def ride(desert, n):
    car_idx = None
    for i, row in enumerate(desert):
        for j, col in enumerate(row):
            if col == 'c':
                car_idx = [i, j]
                break

    stack = []
    stack.append(car_idx)
    grid_control = {_parse_car_idxs_to_str(car_idx[0], car_idx[1]): n}
    while len(stack) > 0:
        curr_row, curr_col = stack.pop()
        curr_val = desert[curr_row][curr_col]
        if curr_val == 'o':
            return True

        curr_fuel = grid_control[_parse_car_idxs_to_str(curr_row, curr_col)]
        if curr_val in list(map(str, range(1, 10))):
            curr_fuel += int(curr_val)

        for d in dirs:
            r_offset, c_offset = d
            next_row = curr_row + r_offset
            next_col = curr_col + c_offset
            if 0 <= next_row < len(desert) and 0 <= next_col < len(desert[0]):
                next_tile = desert[next_row][next_col]
                if next_tile != '*' and curr_fuel > 0:
                    grid_key = _parse_car_idxs_to_str(next_row, next_col)
                    if grid_key not in grid_control:
                        grid_control[grid_key] = curr_fuel - 1
                        next_idxs = [next_row, next_col]
                        stack.append(next_idxs)

    return False


if __name__ == "__main__":
    print(ride(desert, 3))
