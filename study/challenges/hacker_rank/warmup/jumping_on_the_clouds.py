'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
'''

import os
import re


def _validated_constrains(clouds):
    return (re.match('^[01]+$', ''.join(map(str, clouds)))
            and 2 <= len(clouds) <= 100)


def _check_good_cloud(clouds, target_index):
    return clouds[target_index] == 0


def jumpingOnClouds(clouds):
    if _validated_constrains(clouds):
        current_index = target_index = jumps = 0
        max_index = len(clouds) - 1
        while current_index <= max_index:
            target_index = current_index + 2
            if target_index <= max_index:
                if _check_good_cloud(clouds, target_index):
                    jumps += 1
                    current_index = target_index
                    continue

            target_index = current_index + 1
            if target_index <= max_index:
                if _check_good_cloud(clouds, target_index):
                    jumps += 1
                    current_index = target_index
                    continue

            break

        return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
