'''
https://www.hackerrank.com/challenges/new-year-chaos/problem
'''


def _validate_n_constrains(n):
    return 1 <= n <= 10**5


def _validate_t_constrains(t):
    return 1 <= t <= 10


def _calculate_position_offset(item,
                               ix,
                               queue):
    floor_index = max(item - 2, 0)
    return sum([1 for number in queue[floor_index:ix] if number > item])


def minimumBribes(q):
    bribe_count = 0
    queue = list(map(lambda x: x-1, q))
    for ix, item in enumerate(queue):
        if item - ix > 2:
            print('Too chaotic')
            return

        bribe_count += _calculate_position_offset(item, ix, queue)

    print(bribe_count)


if __name__ == '__main__':
    t = int(input())
    if _validate_t_constrains(t):
        for t_itr in range(t):
            n = int(input())
            if _validate_n_constrains(n):
                q = list(map(int, input().rstrip().split()))
                minimumBribes(q)
