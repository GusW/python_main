'''
file        : ./modmixin.py
test        : ./test_ex1.py
primary     : gustavo.watanabe@gmail.com
description : Mixin class for custom mod logic - Exercise 1 helper logic
'''
from collections import defaultdict, namedtuple


class ModMixin:
    def __init__(self):
        self.mod_conditionals = defaultdict(str)

    conditional_interface = namedtuple('conditional_interface', 'number, string')

    def add_mod_conditional(self, conditional_interface):
        ''' Receives a namedtuple conditional_interface and adds to mod_conditionals
            Values should not be replaced by design, throws an assert error otherwise
        '''
        assert not self.mod_conditionals[conditional_interface.number], \
            'Previous conditional found in dict: %s' % self.mod_conditionals[conditional_interface.number]

        self.mod_conditionals[conditional_interface.number] = conditional_interface.string

    def cast_tuple_to_conditional_interface(self, tuple_element):
        ''' Receives a tuple and returns a conditional_interface
            conditional_interface.number should be an int
            conditional_interface.string should be a non-empty string
        '''
        numeric_value, string_value = tuple_element
        assert isinstance(numeric_value, int), 'First element must be int received %s' % type(numeric_value)
        assert string_value and isinstance(string_value, str),\
            'Second element must be str received %s' % type(string_value)

        return self.conditional_interface(number=numeric_value, string=string_value)

    def add_tuple_to_mod_conditionals(self, tuple_element):
        ''' Receives a tuple and casts to conditional_interface
            Adds the casted conditional_interface to mod_conditionals
            Throws Assert Exception if element is not a tuple
        '''
        assert isinstance(tuple_element, tuple), 'Tuple expected, received %s' % type(tuple_element)

        self.add_mod_conditional(self.cast_tuple_to_conditional_interface(tuple_element))

    def get_custom_mod_nums(self, number):
        ''' Concatenates all ocurrencies of custom mod strings found in mod_conditionals for a given number
            Prints the single numeric number value otherwise
            Throws Assert Exception if no number is passed in
        '''
        assert isinstance(number, int), 'Number must be int, received %s' % type(number)

        return (''.join([self.mod_conditionals.get(v) for v in self.mod_conditionals.keys() if number % v == 0]) or
                number)

    def get_mod_conditionals_for_range(self, range_limit):
        ''' Given a integer limit number, iterates from 1 or -1 printing the existing mod conditions strings
            Returns a generator due to performance on large range limits
            Throws Assert Exception if no integer is passed in
        '''
        assert range_limit and isinstance(range_limit, int), 'Range must be int != 0, received %s' % range_limit
        sign = 1 if range_limit > 0 else -1
        start, end, step = sign, range_limit + sign, sign
        return (self.get_custom_mod_nums(number) for number in range(start, end, step))
