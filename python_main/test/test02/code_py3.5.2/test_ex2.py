'''
file        : ./test_ex2.py
primary     : gustavo.watanabe@gmail.com
description : unittests for ./ex2.py file
              tests every single class method and assert given solutions to other scenarions
'''
# Python imports
import unittest

from ex2 import Exercise2
from postcodemixin import PostcodeMixin, PostcodeConstructorMap


class UKPostcodeConstructorTests(unittest.TestCase):
    def setUp(self):
        self.uk = PostcodeConstructorMap.UK.value

    def test__validate_area(self):
        self.assertTrue(self.uk._validate_area('A'))
        self.assertTrue(self.uk._validate_area('AA'))
        self.assertFalse(self.uk._validate_area('X'))
        self.assertFalse(self.uk._validate_area('AZ'))
        self.assertFalse(self.uk._validate_area('AAA'))

    def test__validate_district(self):
        # Single Area code
        self.assertFalse(self.uk._validate_district('S', 'A9'))

        self.assertTrue(self.uk._validate_district('B', '9'))
        self.assertTrue(self.uk._validate_district('S', '99'))
        self.assertFalse(self.uk._validate_district('M', '995'))

        self.assertTrue(self.uk._validate_district('N', '1C'))
        self.assertTrue(self.uk._validate_district('S', '9U'))
        self.assertFalse(self.uk._validate_district('T', '8I'))

        # Double Area code
        self.assertTrue(self.uk._validate_district('CM', '0'))
        self.assertFalse(self.uk._validate_district('CN', '0'))

        self.assertTrue(self.uk._validate_district('LL', '10'))
        self.assertFalse(self.uk._validate_district('AB', '1'))

        self.assertTrue(self.uk._validate_district('HA', '1'))
        self.assertFalse(self.uk._validate_district('LD', '99'))

        self.assertTrue(self.uk._validate_district('BS', '10'))
        self.assertTrue(self.uk._validate_district('BS', '1'))

        self.assertTrue(self.uk._validate_district('NW', '1W'))
        self.assertFalse(self.uk._validate_district('NW', '2W'))

        self.assertTrue(self.uk._validate_district('EC', '1P'))
        self.assertFalse(self.uk._validate_district('WC', '2Z'))

    def test__validate_sector(self):
        self.assertTrue(self.uk._validate_sector('0'))
        self.assertTrue(self.uk._validate_sector('9'))
        self.assertFalse(self.uk._validate_sector('19'))
        self.assertFalse(self.uk._validate_sector('a'))

    def test__validate_unit(self):
        self.assertTrue(self.uk._validate_unit('AA'))
        self.assertTrue(self.uk._validate_unit('ZZ'))
        self.assertTrue(self.uk._validate_unit('AZ'))
        self.assertFalse(self.uk._validate_unit('AV'))
        self.assertFalse(self.uk._validate_unit('ZO'))
        self.assertFalse(self.uk._validate_unit('AAA'))

    def test_trim_postcode(self):
        self.assertEqual(self.uk.trim_postcode('a ! 1  "1 ~9 a a  '), 'a119aa')
        self.assertEqual(self.uk.trim_postcode('a119aa'), 'a119aa')
        self.assertEqual(self.uk.trim_postcode(('a', '!', '1', '"1', '~9', 'a', 'a', '  ')), 'a119aa')

    def test_slice_postcode(self):
        self.assertEqual(self.uk.slice_postcode('a ! 1  "1 ~9 a a  '), ('a', '11', '9', 'aa'))
        self.assertEqual(self.uk.slice_postcode('a ! "1 a ~9 a a  '), ('a', '1a', '9', 'aa'))
        self.assertEqual(self.uk.slice_postcode('a !a "1 a $$ ~9 a a  '), ('aa', '1a', '9', 'aa'))

        with self.assertRaisesRegexp(AssertionError, 'Inward'):
            self.uk.slice_postcode('$$ ~9 a   ')

        with self.assertRaisesRegexp(AssertionError, 'Outward'):
            self.uk.slice_postcode('$$ ~9 a a  ')

        with self.assertRaisesRegexp(AssertionError, 'district'):
            self.uk.slice_postcode('a#a$$ ~9 a a  ')


class PostcodeMixinTests(unittest.TestCase):
    def setUp(self):
        self.post = PostcodeMixin()
        self.uk_constructor = PostcodeConstructorMap.UK.value

    def test__param_type_checker(self):
        with self.assertRaisesRegexp(AssertionError, 'int'):
            self.post._param_type_checker(2, str)

        with self.assertRaisesRegexp(AssertionError, 'str'):
            self.post._param_type_checker('2', int)

        # If no AssertionError the function returns nothing
        self.assertFalse(self.post._param_type_checker(2, int))

    def test__param_exists_checker(self):
        with self.assertRaisesRegexp(AssertionError, '2'):
            self.post._param_exists_checker(None, 2)

        # If no AssertionError the function returns nothing
        self.assertFalse(self.post._param_exists_checker(2, 2))

    def test_get_constructor_for_region(self):
        self.assertEqual(self.post.get_constructor_for_region('UK'), PostcodeConstructorMap.UK.value)
        self.assertEqual(self.post.get_constructor_for_region('ARG'), PostcodeConstructorMap.ARG.value)
        self.assertEqual(self.post.get_constructor_for_region('BRA'), PostcodeConstructorMap.BRA.value)
        self.assertIsNone(self.post.get_constructor_for_region('IRE'))

    def test_get_action_for_constructor(self):
        self.assertEqual(self.post.get_action_for_constructor(self.uk_constructor, 'formats'),
                         self.uk_constructor.formats)
        self.assertEqual(self.post.get_action_for_constructor(self.uk_constructor, 'validates'),
                         self.uk_constructor.validates)
        self.assertIsNone(self.post.get_action_for_constructor(self.uk_constructor, 'creates'))

    def test_postcode_action(self):
        mocked_postcode_1 = 'a99aa'
        self.assertEqual(self.post.postcode_action(mocked_postcode_1, 'uk', 'validates'),
                         self.uk_constructor.validates(mocked_postcode_1))

        self.assertEqual(self.post.postcode_action(mocked_postcode_1, 'uk', 'formats'),
                         self.uk_constructor.formats(mocked_postcode_1))

        with self.assertRaisesRegexp(AssertionError, 'int'):
            self.post.postcode_action(2, 'uk', 'formats')

        with self.assertRaisesRegexp(AssertionError, 'tuple'):
            self.post.postcode_action(mocked_postcode_1, ('uk',), 'formats')

        with self.assertRaisesRegexp(AssertionError, 'list'):
            self.post.postcode_action(mocked_postcode_1, 'uk', ['formats'])


class Exercise2Tests(unittest.TestCase):
    def setUp(self):
        self.ex = Exercise2()

    def test_postcode_API(self):
        valid_postcodes = ['M1 1AE', 'B33 8TH', 'W1A 0AX', 'CR2 6XH', 'DN55 1PT', 'EC1A 1BB', 'GIR 0AA', 'W1J 7NT',
                           'DE12 8HJ', 'SW1A 1AA', 'HD7 5UZ', 'CH5 3QW', 'CH5 3QW', 'PL7 1RF', 'JE3 1EP', 'JE2 3XP',
                           'IM9 4EB', 'IM9 4AJ', 'GY7 9YH', 'LL59 5PD']
        for code in valid_postcodes:
            self.assertTrue(self.ex.postcode_API(code))

        unformatted_postcodes = ['m11Ae', 'IM94aj', 'LL595P D', 'je31ep', 'a a 1 a 9 a a   ']
        for code in unformatted_postcodes:
            formatted_postcode = self.ex.postcode_API(code, action="formats")
            self.assertRegex(formatted_postcode, r'^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$')
