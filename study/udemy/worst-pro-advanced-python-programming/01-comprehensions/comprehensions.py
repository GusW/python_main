"""
Python Comprehensions
"""
from pathlib import Path

SEPARATOR = "-"
SEPARATOR_LEN = 20

ROOT_DIR = Path(__file__).parent.parent.resolve()
RESOURCES_DIR = 'resources'
EXAMPLE_FILENAME = 'example.txt'
FILE_PATH = Path.joinpath(ROOT_DIR, RESOURCES_DIR, EXAMPLE_FILENAME)
TARGET_EXP = "here"

nums1 = range(1, 6)
nums2 = range(3, 9)

###### <List Comprehensions

squares = [num**2 for num in nums1]

list_intersection = [num for num in nums1 if num in nums2]

list_outer_difference = [
    num
    for num in [*nums1, *nums2]
    if (num in nums1 and num not in nums2) or (num in nums2 and num not in nums1)
]

print(f"{SEPARATOR_LEN*SEPARATOR} <FILE\n")
with open(FILE_PATH, encoding="utf-8" ) as openedFile:
    target_phrase = [phrase for phrase in openedFile if TARGET_EXP in phrase]
    print(f"{target_phrase=}\n")

with open(FILE_PATH, encoding="utf-8" ) as openedFile:
    list_with_index = [f'{idx} - {phrase}' for idx, phrase in enumerate(openedFile, 1)]
    print(f"{list_with_index=}\n")
print(f"{SEPARATOR_LEN*SEPARATOR} FILE/>\n")

def _squared(num: int| float) -> int | float:
    return num**2

new_squared_list = [_squared(num) for num in nums2]

###### List/> Comprehensions
###### <Dict Comprehensions

dict_with_squares = {num: num**2 for num in nums1}
dict_with_even_squares = {num: num**2 for num in nums2 if num % 2 == 0}

fahrenheit = {'temp1': 10, 'temp2': 20, 'temp3': 30, 'temp4':40}
celsius = {key: (value-32)*(5/9) for key, value in fahrenheit.items()}

###### Dict/> Comprehensions
###### <Set Comprehensions

num_set = {num for num in [*nums1, *nums2]}
num_set_odd = {num for num in [*nums1, *nums2] if num % 2 != 0}

###### Set/> Comprehensions
###### <Generator Comprehensions

gen_nums = (num for num in [*nums1, *nums2])
gen_nums_even = (num for num in [*nums1, *nums2] if num % 2 == 0)

###### Generator/> Comprehensions


if __name__ == "__main__":
    ###### <List Comprehensions

    print(f"{SEPARATOR_LEN*SEPARATOR} <LIST\n")
    print(f"{squares=}\n")
    print(f"{list_intersection=}\n")
    print(f"{list_outer_difference=}\n")
    print(f"{new_squared_list=}\n")
    print(f"{SEPARATOR_LEN*SEPARATOR} LIST/>\n")

    ###### List/> Comprehensions
    ###### <Dict Comprehensions

    print(f"{SEPARATOR_LEN*SEPARATOR} <DICT\n")
    print(f"{dict_with_squares=}\n")
    print(f"{dict_with_even_squares=}\n")
    print(f"{celsius=}\n")
    print(f"{SEPARATOR_LEN*SEPARATOR} DICT/>\n")

    ###### Dict/> Comprehensions
    ###### <Set Comprehensions

    print(f"{SEPARATOR_LEN*SEPARATOR} <SET\n")
    print(f"{num_set=}\n")
    print(f"{num_set_odd=}\n")
    print(f"{SEPARATOR_LEN*SEPARATOR} SET/>\n")

    ###### Set/> Comprehensions
    ###### <Generator Comprehensions

    print(f"{SEPARATOR_LEN*SEPARATOR} <GENERATOR\n")
    print(f"{gen_nums=}\n")
    print(f"{next(gen_nums)=}\n")
    print(f"{gen_nums_even=}\n")
    print(f"{next(gen_nums_even)=}\n")
    print(f"{SEPARATOR_LEN*SEPARATOR} GENERATOR/>\n")

    ###### Generator/> Comprehensions
