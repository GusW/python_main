#!/bin/python3

import os

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

"""
dp[j] stores the number of solutions for j.

For base case j=0, number of solutions is 1(not using any coin).

Now in the for loop, i represents the number of coins you are using.

Initially i=0, so you cannot create change for any j>0, hence dp[j]=0 for j>0.

Now in each iteration you add a new coin and update the number of solutions for those j
which have value not less than the value of ith coin.

This update is just adding the number of solutions when we use the ith coin
which is equal to the number of solutions of creating change for j-coins[i].

We are finally done when we use all the coins and so we print dp[n].
"""


def getWays(n, c):
    dp = [1] + [0]*n                # [1, 0, 0, 0, 0]
    print("begin", dp)               # c = {1, 2, 3}
    for i in range(len(c)):         # 0, 1, 2
        for j in range(c[i], n+1):  # 1 -> 4
            dp[j] += dp[j-c[i]]     # [1, 0 + 1]
        print(dp)

    print("end", dp)
    return dp[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
