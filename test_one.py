from test_one import longestCommonPrefix
import unittest


class TestLongestCommonPrefix(unittest.TestCase):

    def test_longestCommonPrefix(self):
        # Arrange
        words1 = ["apple", "app", "apply"]
        words2 = ["dog", "duck", "dove"]
        words3 = ["flower", "flour", "flew"]

        # Act
        result1 = longestCommonPrefix(words1)
        result2 = longestCommonPrefix(words2)
        result3 = longestCommonPrefix(words3)

        # Assert
        self.assertEqual(result1, "app")
        self.assertEqual(result2, "d")
        self.assertEqual(result3, "fl")


if __name__ == '__main__':
    unittest.main()