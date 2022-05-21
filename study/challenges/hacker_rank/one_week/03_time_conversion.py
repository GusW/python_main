#!/bin/python3
import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    hours, minutes, seconds = f"{s[0]}{s[1]}", f"{s[3]}{s[4]}", f"{s[6]}{s[7]}"
    hours_int = int(hours)
    modifier = f"{s[-2]}{s[-1]}".upper()
    converted_hours = hours
    if modifier == "PM" and hours_int < 12:
        converted_hours = hours_int + 12

    if modifier == "AM" and hours_int == 12:
        converted_hours = '00'

    return f"{converted_hours}:{minutes}:{seconds}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
