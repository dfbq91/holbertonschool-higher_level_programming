#!/usr/bin/python3
'''Test cases for Base module'''
import unittest

class TestBase(unittest.TestCase):
    def test_id_attribute(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4) 
