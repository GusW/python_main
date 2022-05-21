#!/bin/python3

"""
We define super digit of an integer X using the following rules:

Given an integer, we need to find the super digit of the integer.

- If X has only digit, then its super digit is X
- Otherwise, the super digit of X is equal to the super digit of the sum of the digits of X

For example, the super digit of 9875 will be calculated as:

    super_digit(9875)   9+8+7+5 = 29
    super_digit(29) 	2 + 9 = 11
    super_digit(11)		1 + 1 = 2
    super_digit(2)		= 2

Example

N = 9875
K = 4

The number P is created by concatenating the string N K times so the initial P = 9875987598759875

    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)

All of the digits of P sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it is the super digit.

Function Description

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

    string n: a string representation of an integer
    int k: the times to N concatenate to make p

Returns

    int: the super digit of N repeated K times

Input Format

The first line contains two space separated integers, N and K

Constraints
- 1 <= N < 10^100000
- 1 <= K <= 10^5

"""

import os

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


"""
if len(X) == 1 then SD = 1


"""


def superDigit(n, k):
    if len(str(n)) == 1 and k == 1:
        return n

    sd = sum(map(int, list(str(n))))

    return superDigit(str(sd) * k, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
