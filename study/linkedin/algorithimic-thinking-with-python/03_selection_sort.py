def find_min_idx(target_list, idx_offset=0):
    min_idx = 0
    for idx in range(len(target_list)):
        if target_list[idx] < target_list[min_idx]:
            min_idx = idx

    return min_idx + idx_offset


def find_min(xs):
    return xs[find_min_idx(xs)]


def selection_sort(xs):
    for idx in range(len(xs)):
        min_idx = find_min_idx(xs[idx:], idx)
        xs[idx], xs[min_idx] = xs[min_idx], xs[idx]

    return xs


if __name__ == "__main__":
    xs = [3, 2, 1, 5, 4]
    print(xs)
    selection_sort(xs)
    print(xs)
    # A nice Pythonic way to check  a list is sorted
    # without relying on using Python's own sorting methods to compare.
    print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))

    xs = [-4, 2, 6, -8, 16, 25, 7, 3, 2, 1, 5, 4]
    print(xs)
    selection_sort(xs)
    print(xs)
    print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))
