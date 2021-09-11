from unittest import TestCase

from gender_converter import convert_gender


class Test(TestCase):
    def test_convert_gender_when_male(self):
        expected = "MALE"
        actual = convert_gender("M")
        self.assertEqual(actual, expected)

    def test_convert_gender_when_female(self):
        expected = "FEMALE"
        actual = convert_gender("F")
        self.assertEqual(actual, expected)

    def test_convert_gender_when_unknown(self):
        expected = "MALDITO OPRESOR"
        actual = convert_gender("sSs")
        self.assertEqual(actual, expected)

