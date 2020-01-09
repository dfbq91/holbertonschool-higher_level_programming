#!/usr/bin/python3
'''0-square.py: Create a square class with private instance'''


class Square:
    '''class Square'''
    def __init__(self, size=0):
        '''Will initialize square class'''
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
