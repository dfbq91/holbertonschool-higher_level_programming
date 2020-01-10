#!/usr/bin/python3
'''0-square.py: Create a square class with size and area'''


class Square:
    '''class Square'''
    def __init__(self, size=0):
        '''Will initialize square class with size'''
        self.__size = size

    @property
    def size(self):
        '''Returns the size of a square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Defines value of size of square and checks if it's > 0 and an int'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''return current area of a square'''
        return self.__size * self.__size
