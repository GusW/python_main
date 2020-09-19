'''
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
'''

import os
import re


def _satisfied_checked_constrains(steps, path):
    return (2 <= steps <= 10**6
            and re.match('^[UD]+$', path))


def _evaluate_changed_level(current_level, path_entry):
    return current_level + (1 if path_entry.upper() == 'U'
                            else -1)


def countingValleys(steps, path):
    if _satisfied_checked_constrains(steps, path):
        current_level = valleys = 0
        for entry in path:
            target_level = _evaluate_changed_level(current_level, entry)
            if (current_level == 0 and target_level < 0):
                valleys += 1
            current_level = target_level

        return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
