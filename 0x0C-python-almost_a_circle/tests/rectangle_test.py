#!/usr/bin/python3
'''Test cases for Rectangle module'''
import unittest

class TestRectangle(unittest.TestCase):
    def test_creation_rectangle(self):
        '''Check if rentangle is correctly created'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_error_messages(self):
        '''Make sure value errors are raised'''
        self.assertRaises(TypeError, Rectangle, (5, 'h'))
        self.assertRaises(TypeError, Rectangle, ('2', 4))
        self.assertRaises(TypeError, Rectangle, (5, 2, {2}, 12))
        self.assertRaises(TypeError, Rectangle, (5, 2, 3, [2, 3]))
        self.assertRaises(ValueError, Rectangle, (5, -3))
        self.assertRaises(ValueError, Rectangle, (0, 3))
        self.assertRaises(ValueError, Rectangle, (8, 3, -5, 5))
        self.assertRaises(ValueError, Rectangle, (8, 3, 5, 0))

    def test_area_rectangle(self):
        '''Check if the area is correctly calculated'''
        a1 = Rectangle(10, 2)
        self.assertEqual(a1.area, 20)

    def test_str_method(self):
        '''Check if the str method returns correctly'''
        str1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str1, Rectangle(4, 6, 2, 1, 12))
        str1 = "Rectangle(5, 5, 1)"
        self.assertEqual(str1, Rectangle(5, 5, 1))
