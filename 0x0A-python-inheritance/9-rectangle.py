#!/usr/bin/python3
'''Module that inherits from 7-base_geometry.py'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass of BaseGeometry'''
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''calculates the area'''
        return self.__width * self.__height

    def __str__(self):
        '''return width and height of rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
