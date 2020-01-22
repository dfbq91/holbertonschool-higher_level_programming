#!/usr/bin/python3
'''task 12'''

class Student:
    '''class with student elements'''
    def __init__(self, first_name, last_name, age):
        '''init values for object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            new_dict = {}
            for element in attrs:
                if hasattr(self, element):
                    new_dict[element] = getattr(self, element)
        elif not attrs:
            return self.__dict__
        return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
