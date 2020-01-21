#!/usr/bin/python3
'''function with issubclass'''


def inherits_from(obj, a_class):
    '''returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified
    class; otherwise False'''
    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
