#!/usr/bin/python3
'''
Script to add two integers
'''


def add_integer(a, b=98):
    '''
    add a and b if they are integers
    '''
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
