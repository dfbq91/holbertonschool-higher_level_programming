#!/usr/bin/python3
'''Module that creates a new class'''


class BaseGeometry:
    '''class with one method'''
    def area(self):
        '''show error message for area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates if value isn't an integer or if it's less or equal to 0'''
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
