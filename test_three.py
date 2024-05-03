from test_three import roman_to_arabic
import unittest


class TestRomanToArabic(unittest.TestCase):

    def test_valid_roman_numbers(self):
        self.assertEqual(roman_to_arabic('I'), 1)
        self.assertEqual(roman_to_arabic('V'), 5)

    def test_invalid_roman_numbers(self):
        self.assertEqual(roman_to_arabic('IIII'), 'Invalid Entry')
        self.assertEqual(roman_to_arabic('IXI'), 'Invalid Entry')

    def test_edge_cases(self):
        self.assertEqual(roman_to_arabic(''), 'Invalid Entry')
        self.assertEqual(roman_to_arabic(123), 'Invalid Entry')



if __name__ == '__main__':
    unittest.main()