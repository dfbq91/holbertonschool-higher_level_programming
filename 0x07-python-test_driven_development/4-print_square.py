#!/usr/bin/python3
'''Script to print a square'''


def print_square(size):
    '''function that prints a square with the character #'''
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print('#', end='')
        print()
