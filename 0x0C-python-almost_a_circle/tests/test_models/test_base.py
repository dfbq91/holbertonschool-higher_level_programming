#!/usr/bin/python3
'''Test cases for Base module'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

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
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        '''Para hacer alguna acción al final de los casos de testeo.
        Implica colocar self en cada objeto creado y self donde se
        haga mención a este objeto'''
        pass

    def test_id_attribute(self):
        Base._Base__nb_objects = 0
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
