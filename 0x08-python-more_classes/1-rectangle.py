#!/usr/bin/python3
'''Module that creates a new class'''


class Rectangle:
    '''Class with width and height'''
    def __init__(self, width=0, height=0):
        '''init values for an object of rectangle class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Returns width value assign to an object(rectangle)'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Assign a value to a width of object(rectangle)'''
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''Returns height value assign to an object(rectangle)'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
