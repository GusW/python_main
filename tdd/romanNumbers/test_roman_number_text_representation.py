from unittest import TestCase
from roman_number_text_representation import RomanNumberTextRepresentation


class RomanNumberTextRepresentationTest(TestCase):
    def test_001(self):
        self.assertEquals("I", RomanNumberTextRepresentation.of(1))

    def test_002(self):
        self.assertEquals("II", RomanNumberTextRepresentation.of(2))

    def test_003(self):
        self.assertEquals("III", RomanNumberTextRepresentation.of(3))

    def test_004(self):
        self.assertEquals("IV", RomanNumberTextRepresentation.of(4))

    def test_005(self):
        self.assertEquals("V", RomanNumberTextRepresentation.of(5))

    def test_006(self):
        self.assertEquals("VI", RomanNumberTextRepresentation.of(6))

    def test_007(self):
        self.assertEquals("VII", RomanNumberTextRepresentation.of(7))

    def test_008(self):
        self.assertEquals("VIII", RomanNumberTextRepresentation.of(8))

    def test_009(self):
        self.assertEquals("IX", RomanNumberTextRepresentation.of(9))

    def test_010(self):
        self.assertEquals("X", RomanNumberTextRepresentation.of(10))

    def test_011(self):
        self.assertEquals("XI", RomanNumberTextRepresentation.of(11))

    def test_012(self):
        self.assertEquals("XII", RomanNumberTextRepresentation.of(12))

    def test_013(self):
        self.assertEquals("XIII", RomanNumberTextRepresentation.of(13))

    def test_014(self):
        self.assertEquals("XIV", RomanNumberTextRepresentation.of(14))

    def test_015_to_018(self):
        self.assertEquals("XV", RomanNumberTextRepresentation.of(15))
        self.assertEquals("XVI", RomanNumberTextRepresentation.of(16))
        self.assertEquals("XVII", RomanNumberTextRepresentation.of(17))
        self.assertEquals("XVIII", RomanNumberTextRepresentation.of(18))

    def test_019(self):
        self.assertEquals("XIX", RomanNumberTextRepresentation.of(19))

    def test_020_to_029(self):
        self.assertEquals("XX", RomanNumberTextRepresentation.of(20))
        self.assertEquals("XXIV", RomanNumberTextRepresentation.of(24))
        self.assertEquals("XXVI", RomanNumberTextRepresentation.of(26))
        self.assertEquals("XXIX", RomanNumberTextRepresentation.of(29))

    def test_030_to_039(self):
        self.assertEquals("XXX", RomanNumberTextRepresentation.of(30))
        self.assertEquals("XXXIV", RomanNumberTextRepresentation.of(34))
        self.assertEquals("XXXVI", RomanNumberTextRepresentation.of(36))
        self.assertEquals("XXXIX", RomanNumberTextRepresentation.of(39))

    def test_040_to_049(self):
        self.assertEquals("XL", RomanNumberTextRepresentation.of(40))
        self.assertEquals("XLIV", RomanNumberTextRepresentation.of(44))
        self.assertEquals("XLVI", RomanNumberTextRepresentation.of(46))
        self.assertEquals("XLIX", RomanNumberTextRepresentation.of(49))

    def test_050_to_089(self):
        self.assertEquals("L", RomanNumberTextRepresentation.of(50))
        self.assertEquals("LXIX", RomanNumberTextRepresentation.of(69))
        self.assertEquals("LXXV", RomanNumberTextRepresentation.of(75))
        self.assertEquals("LXXVIII", RomanNumberTextRepresentation.of(78))
        self.assertEquals("LXXXIX", RomanNumberTextRepresentation.of(89))

    def test_090_to_099(self):
        self.assertEquals("XC", RomanNumberTextRepresentation.of(90))
        self.assertEquals("XCIV", RomanNumberTextRepresentation.of(94))
        self.assertEquals("XCVI", RomanNumberTextRepresentation.of(96))
        self.assertEquals("XCIX", RomanNumberTextRepresentation.of(99))

    def test_100_to_999(self):
        self.assertEquals("C", RomanNumberTextRepresentation.of(100))
        self.assertEquals("CCXXIV", RomanNumberTextRepresentation.of(224))
        self.assertEquals("CCCXXXVI", RomanNumberTextRepresentation.of(336))
        self.assertEquals("CDVII", RomanNumberTextRepresentation.of(407))
        self.assertEquals("DCVIII", RomanNumberTextRepresentation.of(608))
        self.assertEquals("DCCCLXXXVIII", RomanNumberTextRepresentation.of(888))
        self.assertEquals("CMXCIX", RomanNumberTextRepresentation.of(999))
