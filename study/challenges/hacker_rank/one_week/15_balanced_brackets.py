#!/bin/python3

import os


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

bracket_map = {
    "}": "{",
    "]": "[",
    ")": "("
}


def isBalanced(s):
    stack = []
    arr = list(s)
    for char in arr:
        target_pair = bracket_map.get(char)
        if target_pair:
            if stack and stack[-1] == target_pair:
                stack.pop()
            else:
                return 'NO'
        else:
            stack.append(char)

    return 'YES' if not stack else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
