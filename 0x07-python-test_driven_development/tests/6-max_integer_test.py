#!/usr/bin/python3
'''Test cases for a function that gets highest integer'''
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        '''Test if the function get the max integer in a list'''
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_no_arguments(self):
        '''Test when there aren't arguments in fun'''
        self.assertEqual(max_integer(), None)

    def test_if_is_LofList(self):
        '''Test if arguments given is list of lists'''
        self.assertEqual(max_integer([[1, 2, 3], [6, 2, 9]]), [6, 2, 9])

    def test_negative(self):
        '''Test when negative numbers are given'''
        self.assertTrue(max_integer([-1, -2, -3, -4]) == -1)

    def test_just_one_number(self):
        '''Test when the list has just one number'''
        self.assertEqual(max_integer([6]), 6)

    def test_same_number(self):
        '''Test when the list has the same number'''
        self.assertEqual(max_integer([12, 12, 12, 12, 12, 12]), 12)

    def test_floats(self):
        '''Test when there are floats given'''
        self.assertEqual(max_integer([12.3, 19.2, 29.4, -65.512]), 29.4)

    def test_error_different_to_int(self):
        '''Make sure value errors are raised'''
        self.assertRaises(TypeError, max_integer, [1, 2, 'e', 4])

    def test_error_different_to_list(self):
        '''Test if the list is empty'''
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    if __name__ == '__main__':
        unittest.main()
