import random


def binary_search_iterative(data, target):
    low_pointer = 0
    high_pointer = len(data) - 1
    while low_pointer <= high_pointer:
        mid_point = (low_pointer + high_pointer) // 2
        if data[mid_point] == target:
            return mid_point
        elif data[mid_point] < target:
            low_pointer = mid_point + 1
        else:
            high_pointer = mid_point - 1
    return -1


def binary_search(data, target):
    def _subproblem(start_idx, end_idx):
        if data[start_idx] == target:
            return start_idx
        if data[end_idx] == target:
            return end_idx

        if start_idx == end_idx:
            return -1

        mid_idx = (start_idx + end_idx) // 2
        mid_val = data[mid_idx]
        if mid_val == target:
            return mid_idx

        if mid_val < target:
            return _subproblem(mid_idx, end_idx)
        else:
            return _subproblem(start_idx, mid_idx)

    start_idx = 0
    end_idx = len(data) - 1
    return _subproblem(start_idx, end_idx)


if __name__ == "__main__":
    n = 10
    max_val = 100
    data = [random.randint(1, max_val) for i in range(n)]
    data.sort()
    print("Data:", data)
    target = int(input("Enter target value: "))
    target_pos = binary_search(data, target)
    if target_pos == -1:
        print("Your target value is not in the list.")
    else:
        print("You target value has been found at index", target_pos)
