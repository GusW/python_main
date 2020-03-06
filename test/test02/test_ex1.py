'''
file        : ./test.py
primary     : gustavo.watanabe@gmail.com
description : unittests for ./ex1.py file
              tests every single class method and assert given solutions to other scenarions
'''
# Python imports
import re
import unittest

from modmixin import ModMixin
from ex1 import Exercise1


class ModMixinTests(unittest.TestCase):
    def setUp(self):
        self.mod = ModMixin()

    def _build_condition(self, condition_type=None):
        ''' Build conditional interface helper function
            If no condition_type, returns condition(10,'Ten')
            If condition_type is 'same', returns condition(10,'Dix')
            If condition_type is 'new', returns condition(11,'Eleven')
        '''
        numeric_val, eng_val, french_val = 10, 'Ten', 'Dix'
        new_numeric_val, new_eng_val = 11, 'Eleven'
        if condition_type == 'same':
            return (numeric_val, french_val, self.mod.conditional_interface(number=numeric_val, string=french_val))
        elif condition_type == 'new':
            return (new_numeric_val, new_eng_val,
                    self.mod.conditional_interface(number=new_numeric_val, string=new_eng_val))
        else:
            return (numeric_val, eng_val, self.mod.conditional_interface(number=numeric_val, string=eng_val))

    def test_add_mod_conditional(self):
        ''' Attest ModMixin.add_mod_conditional
            Should throws assertion error exception when numbers previously added are being replaced
            Should update successfully mod_conditionals for new elements
        '''
        numeric_val, eng_val, condition = self._build_condition()
        self.mod.add_mod_conditional(condition)
        self.assertEqual(self.mod.mod_conditionals[numeric_val], eng_val)

        *_, same_condition = self._build_condition('same')
        with self.assertRaisesRegexp(AssertionError, eng_val):
            self.mod.add_mod_conditional(same_condition)

        new_numeric_val, new_eng_val, new_condition = self._build_condition('new')
        self.mod.add_mod_conditional(new_condition)
        self.assertEqual(self.mod.mod_conditionals[new_numeric_val], new_eng_val)

    def test_cast_tuple_to_conditional_interface(self):
        ''' Attest ModMixin.cast_tuple_to_conditional_interface
            Should throws assertion error exception when params are bad
            Should return a valid conditional interface when params are good
        '''
        numeric_val, string_val = 1, 'One'
        with self.assertRaisesRegexp(AssertionError, 'int'):
            self.mod.cast_tuple_to_conditional_interface((numeric_val, numeric_val))

        with self.assertRaisesRegex(AssertionError, 'str'):
            self.mod.cast_tuple_to_conditional_interface((string_val, string_val))

        cond_interface = self.mod.cast_tuple_to_conditional_interface((numeric_val, string_val))
        self.assertEqual(cond_interface, self.mod.conditional_interface(number=numeric_val, string=string_val))

    def test_add_tuple_to_mod_conditionals(self):
        ''' Attest ModMixin.add_tuple_to_mod_conditionals
            Should throws assertion error exception when element passed in is not a tuple
            Should update successfully mod_conditionals for new elements
        '''
        with self.assertRaisesRegexp(AssertionError, 'int'):
            self.mod.add_tuple_to_mod_conditionals(2)

        with self.assertRaisesRegexp(AssertionError, 'dict'):
            self.mod.add_tuple_to_mod_conditionals({'a': 1})

        numeric_val, string_val = 2, 'Zwei'
        self.mod.add_tuple_to_mod_conditionals((numeric_val, string_val))
        self.assertEqual(self.mod.mod_conditionals[numeric_val], string_val)

    def test_get_custom_mod_nums(self):
        ''' Attest ModMixin.cast_tuple_to_conditional_interface
            Should throws assertion error exception when an int is not passed in
            Should return a valid join of existing
        '''
        with self.assertRaisesRegexp(AssertionError, 'str'):
            self.mod.get_custom_mod_nums('100')

        # Passing a number to the method when empty conditionals should return the numeric value
        numeric_val, eng_val, condition = self._build_condition()
        self.assertEqual(self.mod.get_custom_mod_nums(numeric_val), numeric_val)

        # Passing a number to the method after adding its conditional should return the string value for its multiples
        self.mod.add_mod_conditional(condition)
        self.assertEqual(self.mod.get_custom_mod_nums(numeric_val*2), ''.join([eng_val]))

        # Should return a concatenation of multiple strings if the number is multiple of more than one condition
        mew_numeric_val, new_eng_val, new_condition = self._build_condition('new')
        self.mod.add_mod_conditional(new_condition)

        self.assertEqual(self.mod.get_custom_mod_nums(numeric_val*mew_numeric_val), ''.join([eng_val, new_eng_val]))

    def test_get_mod_conditionals_for_range(self):
        ''' Attest ModMixin.iterate_over_mod_conditionals
            Should throws assertion error exception when an int diff than zero is not passed in
            Should return a valid generator with the same size of the given limit
        '''
        with self.assertRaisesRegexp(AssertionError, '100'):
            self.mod.get_mod_conditionals_for_range('100')

        with self.assertRaisesRegexp(AssertionError, '0'):
            self.mod.get_mod_conditionals_for_range(0)

        limit = 100
        mod_generator = self.mod.get_mod_conditionals_for_range(limit)
        self.assertTrue(mod_generator.__iter__)
        self.assertEqual(len(list(mod_generator)), limit)

        neg_limit = -45
        neg_mod_generator = self.mod.get_mod_conditionals_for_range(neg_limit)
        self.assertTrue(neg_mod_generator.__iter__)
        self.assertEqual(len(list(neg_mod_generator)), abs(neg_limit))


class Exercise1Tests(unittest.TestCase):
    def setUp(self):
        self.ex = Exercise1()

    def test_exercise_API(self):
        ''' Attest Exercise1.exercise_API
            Should return a valid generator with the same size of the given limit
        '''
        cond_numer_two, cond_string_two = 2, 'Two'
        cond_numer_seven, cond_string_seven = 7, 'Seven'
        conditional_two = (cond_numer_two, cond_string_two)
        conditional_seven = (cond_numer_seven, cond_string_seven)
        limit = cond_numer_two * cond_numer_seven

        res = list(self.ex.exercise_API([conditional_two, conditional_seven], limit))

        self.assertEqual(len(res), limit)
        self.assertEqual(len(re.findall(cond_string_two, ' '.join(map(str, res)))), (limit/cond_numer_two))
        self.assertEqual(len(re.findall(cond_string_seven, ' '.join(map(str, res)))), (limit/cond_numer_seven))
        self.assertEqual(res.count(''.join([cond_string_two, cond_string_seven])),
                         limit/(cond_numer_two*cond_numer_seven))
