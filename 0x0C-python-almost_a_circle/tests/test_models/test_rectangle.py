#!/usr/bin/python3
'''Test cases for Rectangle module'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO
import os


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Esto es útil si se quiere hacer algo solo una vez al principio
        y es muy costoso hacerlo para cada caso de testeo'''
        pass

    @classmethod
    def tearDownClass(cls):
        '''Esto es útil si se quiere hacer algo solo una vez al final
        y es muy costoso hacerlo para cada caso de testeo'''
        pass

    def setUp(self):
        '''Para fijar valores que quiero que esten presentes al inicio
        en todos los demás casos de testeo. Implica colocar self en
        cada objeto creado y self donde se haga mención a este objeto'''
        pass

    def tearDown(self):
        '''Para hacer alguna acción al final de los casos de testeo.
        Implica colocar self en cada objeto creado y self donde se
        haga mención a este objeto'''
        pass

    def test_creation_rectangle(self):
        '''Check if rentangle is correctly created(task 2)'''
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_error_messages(self):
        '''Make sure value errors are raised (task 3)'''
        Base._Base__nb_objects = 0
        self.assertRaises(TypeError, Rectangle, (5, 'h'))
        self.assertRaises(TypeError, Rectangle, ('2', 4))
        self.assertRaises(TypeError, Rectangle, (5, 2, {2}, 12))
        self.assertRaises(TypeError, Rectangle, (5, 2, 3, [2, 3]))
        with self.assertRaises(ValueError):
            Rectangle(height=5, width=-3)
            Rectangle(0, 3)
            Rectangle, (8, 3, -5, 5)
            ValueError, Rectangle, (8, 3, 5, 0)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "5", 'h')
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 5, 'h')
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 5, 0)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -5, 3)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 5, 3, -2, 4)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 5, 3, 2, -4)

    def test_area_rectangle(self):
        '''Check if the area is correctly calculated (task 4)'''
        Base._Base__nb_objects = 0
        a1 = Rectangle(10, 2)
        self.assertEqual(a1.area(), 20)
        a2 = Rectangle(10, 3)
        self.assertEqual(a2.area(), 30)
        a3 = Rectangle(10, 3, 0, 0, 8)
        self.assertEqual(a3.area(), 30)
        with self.assertRaises(TypeError):
            r1 = Rectangle()
            self.r1.area(1)

    @unittest.skip("corregir test")
    def test_display_0(self):
        '''Check if display as # to stdout is the expected (task 5)'''
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6)
        result = """####
        ####
        ####
        ####
        ####
        ####"""
        self.assertEqual(r1.display, result)

    def test_str_method(self):
        '''Check if the str method returns correctly (task 6)'''
        Base._Base__nb_objects = 0
        str1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str1, str(Rectangle(4, 6, 2, 1, 12)))
        str1 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str1, str(Rectangle(5, 5, 1)))

    @unittest.skip("corregir test")
    def test_display_1(self):
        '''Check if display as # with x, yto stdout is
        the expected (task 7)'''
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2)
        result = """

        ###
        ###
        ###
        """
        self.assertEqual(r1.display.__str__(), result)

    def test_update_0(self):
        '''check if *args are working well'''
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_1(self):
        '''check if *kwargs are working well'''
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/89")
        r1.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
