from multiprocessing import Pool
from functools import partial


def _validate_n_constrains(n):
    return 1 <= n <= 10**5


def _validate_t_constrains(t):
    return 1 <= t <= 10


def _calculate_position_offset(item,
                               queue=None):
    idx_modified = queue.index(item) + 1
    if item - idx_modified > 2:
        raise Exception()

    floor_index = max(item - 2, 0)
    return sum([1 for number in queue[floor_index:idx_modified - 1] if number > item])


def minimumBribes(q):
    q_size = len(q)
    pool_bucket_size = 10**4
    pool_size = (q_size//pool_bucket_size) or 1
    pool = Pool(pool_size)
    partial_calc = partial(_calculate_position_offset, queue=q)
    try:
        result = pool.map(partial_calc, q)
        print(sum(result))
    except Exception:
        print('Too chaotic')

    pool.terminate()


if __name__ == '__main__':
    t = int(input())
    if _validate_t_constrains(t):
        for t_itr in range(t):
            n = int(input())
            if _validate_n_constrains(n):
                q = list(map(int, input().rstrip().split()))
                minimumBribes(q)
