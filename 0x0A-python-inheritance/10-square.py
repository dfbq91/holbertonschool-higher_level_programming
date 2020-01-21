#!/usr/bin/python3
'''Module that inherits from 9-rectangle.py'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Subclass of Rectangle'''
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''calculates the area'''
        return self.__size * self.__size
