"""
https://app.codility.com/programmers/challenges/yttrium2019/

You are given a string S consisting of N characters and an integer K. You can modify string S by removing any substring of it. A substring is defined as a contiguous segment of a string.

The goal is to find the shortest substring of S that, after removal, leaves S containing exactly K different characters.

Write a function:

def solution(S, K)

that, given a non-empty string S consisting of N characters and an integer K, returns the length of the shortest substring that can be removed. If there is no such substring, your function should return −1.

Examples:

1. Given S = "abaacbca" and K = 2, your function should return 3. After removing substring "cbc", string S will contain exactly two different characters: a and b.

2. Given S = "aabcabc" and K = 1, your function should return 5. After removing "bcabc", string S will contain exactly one character: a.

3. Given S = "zaaaa" and K = 1, your function should return 1. You can remove only one letter: z.

4. Given S = "aaaa" and K = 2, your function should return −1. There is no such substring of S that, after removal, leaves S containing exactly 2 different characters.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
string S consists only of lowercase letters (a−z);
K is an integer within the range [0..26].
"""
from collections import Counter, deque


def solution(S, K):
    if K == 0:
        return len(S)

    account = deque()
    digits = Counter(S)
    for d in digits:
        print(f'd = {d}')
        counter = K
        temp_string = S.replace(d, "1")
        print(f'start = {temp_string}')
        counter -= 1
        curr_idx = 0
        while curr_idx <= len(temp_string) - 1:
            char = temp_string[curr_idx]
            print(f'char = {char}')
            print(f'middle = {temp_string}')
            if char not in ("0", "1"):
                if (counter and ((curr_idx > 0 and temp_string[curr_idx - 1] == "1")
                   or (curr_idx < len(temp_string) - 2 and temp_string[curr_idx + 1] == "1"))):
                    temp_string = temp_string.replace(char, "1")
                    counter -= 1
                else:
                    temp_string = temp_string.replace(char, "0")

            curr_idx += 1
        if "0" in temp_string:
            first_false = temp_string.index("0")
            print(f' temp_string = {temp_string}')
            print(f' last_false_idx = {temp_string[::-1].index("0")}')
            last_false = len(temp_string) - temp_string[::-1].index("0")
            print(f' first_false = {first_false}, last_false={last_false}')
            subs_len = last_false - first_false
        else:
            subs_len = -1 if counter else 0

        account.append(subs_len)

    print(f'===res=={min(account)}')
    return min(account)


def main():
    S = "aaaaazzzzzzzzzzqqq"  # "erqmfuvnng"     # "b"        # "aaaa"  # "zaaaa"  # "aabcabc"  # "abaacbca"
    K = 2   # 1       # 0         # 2       # 1        # 1          # 2
    return solution(S, K)


if __name__ == "__main__":
    main()
