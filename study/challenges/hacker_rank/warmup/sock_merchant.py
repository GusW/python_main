'''
https://www.hackerrank.com/challenges/sock-merchant/leaderboard?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
'''
import os


def _passed_constrains(n, ar):
    return (1 <= n <= 100
            and len(ar) == n)


def sockMerchant(n, ar):
    if _passed_constrains(n, ar):
        unique_numbers = set(ar)
        pair_numbers = [ar.count(num)//2 for num in unique_numbers]
        return sum(pair_numbers)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
