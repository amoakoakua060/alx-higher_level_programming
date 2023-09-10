#!/usr/bin/python3

"""Unittests for max_integer(list) function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test ordered list of integers."""
        _list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(_list), 5)

    def test_unordered_list(self):
        """Test unordered list of integers."""
        _list = [1, 5, 2, 4, 3]
        self.assertEqual(max_integer(_list), 5)

    def test_max_at_begginning(self):
        """Test list which begins with max value."""
        _list = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(_list), 5)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test single element list"""
        _list = [7]
        self.assertEqual(max_integer(_list), 7)

    def test_floats(self):
        """Test a list of floats."""
        _list = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(_list), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        _list = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(_list), 15.5)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Akua"), 'u')

    def test_list_of_strings(self):
        """Test a list of strings."""
        _list = ["My", "name", "is", "Akua"]
        self.assertEqual(max_integer(_list), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
