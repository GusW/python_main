#!/bin/python3

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

"""
    res = 0

    def subproblem(p_idx, res):
        val = q[p_idx]
        # print(f"val:{val}")
        # print(f"p_idx:{p_idx}")
        if val - 1 - p_idx > 2:
            print('Too chaotic')
        else:
            # print(f"p_idx:{p_idx}")
            if p_idx > 0:
                if val < q[p_idx - 1]:
                    res += (q[p_idx - 1] - val)
                    # print(f"q[p_idx - 1]:{q[p_idx - 1]}")
                    # print(f"res:{res}")

                return subproblem(p_idx -1, res)

            print(res)

    return subproblem(len(q) - 1, res)
"""

"""
queue 1 -> N
    0 1 2 3 4

    1 2 3 4 5 6 7 8

    1 2 3 5 4 6 7 8

    1 2 5 3 4 6 7 8

    1 2 5 3 6 4 7 8

    1 2 5 3 6 4 7 8


    1 2 5 3 7 8 6 4
                _2_
              _2_
        _2_
"""

_CHAOTIC_CONSTRAINT = 2


def minimumBribes(q):
    bribe_count = 0
    queue = [x-1 for x in q]

    def _calculate_position_offset(item, ix):
        floor_index = max(item - _CHAOTIC_CONSTRAINT, 0)
        return sum([1 for number in queue[floor_index:ix] if number > item])

    for ix, item in enumerate(queue):
        if item - ix > _CHAOTIC_CONSTRAINT:
            print('Too chaotic')
            return

        bribe_count += _calculate_position_offset(item, ix)

    print(bribe_count)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
