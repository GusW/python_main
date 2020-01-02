'''
file        : ./ex1.py
test        : ./test_ex1.py
primary     : gustavo.watanabe@gmail.com
description : Write a program that prints the numbers from 1 to 100.
              But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”
              For numbers which are multiples of both three and five print “ThreeFive”.
'''
from modmixin import ModMixin


class Exercise1(ModMixin):
    def exercise_API(self, conditionals, limit):
        ''' Receives a list or a single tuple and adds each element to mod_conditionals
            Trigger iteration over range of given positive int limit
        '''
        conditionals = conditionals if isinstance(conditionals, list) else [conditionals]
        for c in conditionals:
            self.add_tuple_to_mod_conditionals(c)

        return self.get_mod_conditionals_for_range(limit)

    def solution(self):
        ''' Lists custom mod conditional for multiples of 3 and for multiples of 5
            Runs to numbers from 1 to 100
            Demonstrates how to use the API passing in any conditional and numeric limit
        '''
        for el in self.exercise_API([(3, 'Three'), (5, 'Five')], 100):
            print(el)

if __name__ == "__main__":
    Exercise1().solution()
