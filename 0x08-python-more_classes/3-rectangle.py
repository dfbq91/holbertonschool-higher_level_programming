#!/usr/bin/python3
'''Module that creates a new class with
width and height, also area and perimeter
methods defined'''


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

    def area(self):
        '''Returns the object(rectangle) area'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns the perimeter of object(rectangle)'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        '''Print the rectangle using #'''
        rect_print = ""
        if self.__width == 0 or self.__height == 0:
            return rec_print
        for y in range(self.__height):
            for x in range(self.__width):
                rect_print += '#'
            if x == self.__width - 1 and y != self.__height - 1:
                rect_print += "\n"
        return rect_print
