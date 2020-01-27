#!/usr/bin/python3
'''Test cases for Square module'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import sys
from io import StringIO
import os


class TestSquare(unittest.TestCase):

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

    def test_creation_square(self):
        '''Check if square is correctly created(task 10)'''
        Base._Base__nb_objects = 0
        str1 = "[Square] (1) 0/0 - 5"
        self.assertEqual(str1, str(Square(5)))
        s1 = Square(5)
        self.assertEqual(s1.id, 2)

    def test_docstring(self):
        '''test if fun, methods, classes and modules have docstring'''
        self.assertIsNotNone(Base.__doc__)

    def test_error_messages(self):
        '''Make sure value errors are raised (task 3)'''
        Base._Base__nb_objects = 0
        self.assertRaises(TypeError, Square, ('h'))
        self.assertRaises(TypeError, Square, (8, '4'))
        self.assertRaises(TypeError, Square, (5, 2, {2}, 12))
        self.assertRaises(TypeError, Square, (5, 2, [2, 3]))
        with self.assertRaises(ValueError):
            Square(size=5, x=-3)
            Square(0, 3)
            Square, (8, 3, -5, 5)
            ValueError, Square, (8, 3, 5, 0)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, 'h')
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, 0)
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 5, -3, -2, 4)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Square, 5, 3, -2, -4)

    def test_area_square(self):
        '''Check if the area is correctly calculated'''
        Base._Base__nb_objects = 0
        a1 = Square(10)
        self.assertEqual(a1.area(), 100)
        a2 = Square(5)
        self.assertEqual(a2.area(), 25)
        with self.assertRaises(TypeError):
            s1 = Square()
            self.s1.area(1)

    def test_display_0(self):
        '''Check if display as # to stdout is the expected (task 5)'''
        var1 = sys.stdout
        sys.stdout = StringIO()
        s1 = Square(4)
        s1.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = var1
        display = "####\n####\n####\n####\n"
        self.assertEqual(display, out)

    def test_str_method(self):
        '''Check if the str method returns correctly (task 6)'''
        Base._Base__nb_objects = 0
        str1 = "[Square] (12) 2/1 - 4"
        self.assertEqual(str1, str(Square(4, 2, 1, 12)))
        str1 = "[Square] (1) 5/1 - 5"
        self.assertEqual(str1, str(Square(5, 5, 1)))

    def test_display_1(self):
        '''Check if display as # with x, y to stdout is
        the expected (task 7)'''
        var1 = sys.stdout
        sys.stdout = StringIO()
        s1 = Square(4, 3, 2, 2)
        s1.display()
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = var1
        display = "\n\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(display, out)

    def test_update_0(self):
        '''check if *args are working well'''
        Base._Base__nb_objects = 0
        s1 = Square(10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")

    def test_update_1(self):
        '''check if *kwargs are working well'''
        Base._Base__nb_objects = 0
        s1 = Square(10, 10, 10)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(size=89)
        self.assertEqual(s1.__str__(), "[Rectangle] (1) 10/10 - 89")
        s1.update(id=89, x=1, size=2, y=3)
        self.assertEqual(s1.__str__(), "[Rectangle] (89) 1/3 - 2")

    def test_update_1(self):
        '''check if def_to_dictionary method returns a dictionary
        representation of a object (task 13)'''
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(),
                         {'x': 2, 'y': 1, 'id': 1, 'size': 10})
