from test_two import find_missing_number
import unittest

def find_missing_number(nums, n):
    total_sum = (n * (n + 1)) // 2
    remaining_sum = sum(nums)
    missing_number = total_sum - remaining_sum
    return missing_number

class TestFindMissingNumber(unittest.TestCase):
    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1, 2, 3, 5], 6), 4)
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5, 6, 7, 9, 10], 11), 8)
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 13), 11)
        self.assertEqual(find_missing_number([1, 3, 2, 4, 8, 9, 10], 11), 5)

if __name__ == '__main__':
    unittest.main()