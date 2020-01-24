#!/usr/bin/python3
'''Base class'''


import json


class Base:
    '''This class will be the “base” of all other classes in this project'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        with open(str(cls.__name__) + ".json", 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                JSON_string_representation = []
                for obj in list_objs:
                    JSON_string_representation.append(obj.to_dictionary())
                my_list = f.write(Base.to_json_string(JSON_string_representation))
            return my_list
