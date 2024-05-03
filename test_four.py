from test_four import are_anagrams
import unittest


class TestAnagrams(unittest.TestCase):
    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("heart", "earth"))
        self.assertTrue(are_anagrams("debit card", "bad credit"))
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertFalse(are_anagrams("python", "java"))

if __name__ == '__main__':
    unittest.main()