'''
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
'''
import os


_TARGET_CHAR = 'a'


def _validated_contrains(s, n):
    return (1 <= len(s) <= 100
            and 1 <= n <= 10**12)


def repeatedString(s, n):
    if _validated_contrains(s, n):
        a_times_in_str = s.count(_TARGET_CHAR)
        times_to_repeat_str = n // len(s)
        remainder_str = n % len(s)
        substring = (a_times_in_str * times_to_repeat_str +
                     [s[i] for i in range(remainder_str)].count(_TARGET_CHAR))
        return substring


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
