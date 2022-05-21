#!/bin/python3

"""
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet,
just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Example

s = There's-a-starman-waiting-in-the-sky
k = 3

The alphabet is rotated by 3, matching the mapping above. The encrypted string is
Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

    string s: cleartext
    int k: the alphabet rotation factor

Returns

    string: the encrypted string

Input Format

The first line contains the integer, N, the length of the unencrypted string.
The second line contains the unencrypted string, S.
The third line contains K, the number of letters to rotate the alphabet by.

Constraints
- 1 <= N <= 100
- 0 <= K <= 100

is a valid ASCII string without any spaces.

Sample Input

11
middle-Outz
2

Sample Output

okffng-Qwvb

Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

"""

import os
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    alphabet_lower = string.ascii_lowercase
    alphabet_size = len(alphabet_lower)
    rotation_factor = k % alphabet_size
    if rotation_factor == 0:
        return s

    def _get_rotation_idx(original_idx: int) -> int:
        new_idx = original_idx + rotation_factor
        if new_idx >= alphabet_size:
            return new_idx - alphabet_size

        return new_idx

    rotation_map = {l: alphabet_lower[_get_rotation_idx(
        idx)] for idx, l in enumerate(alphabet_lower)}

    def _get_letter_rotation(letter: str) -> str:
        rotated_letter = rotation_map.get(letter.lower()) or letter
        return rotated_letter if letter.islower() else rotated_letter.upper()

    return ''.join([_get_letter_rotation(letter) for letter in s])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

    """
    11
    middle-Outz
    2
    """
    """
    38
    Always-Look-on-the-Bright-Side-of-Life
    5
    """
