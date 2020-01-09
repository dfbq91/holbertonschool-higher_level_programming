#!/usr/bin/python3
'''0-square.py: Create a square class with size and area'''


class Square:
    '''class Square'''
    def __init__(self, size=0):
        '''Will initialize square class with size'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''return area of a square'''
        return self.__size * self.__size
