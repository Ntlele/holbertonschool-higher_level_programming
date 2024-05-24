#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        """Test max_integer with list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        # Add more test cases for positive numbers

    def test_negative_numbers(self):
        """Test max_integer with list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # Add more test cases for negative numbers

    def test_mixed_numbers(self):
        """Test max_integer with list of mixed positive and negative integers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        # Add more test cases for mixed numbers

    def test_single_element(self):
        """Test max_integer with single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test max_integer with empty list"""
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
