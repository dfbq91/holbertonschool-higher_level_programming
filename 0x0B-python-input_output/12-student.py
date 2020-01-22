#!/usr/bin/python3
'''task 12'''

class Student:
    '''class with student elements'''
    def __init__(self, first_name, last_name, age):
        '''init values for object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    new_dict = {}
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        for element in attrs:
            if hasattr(self, items):
                new_dict[element] = getattr(self, element)
        return new_dict
