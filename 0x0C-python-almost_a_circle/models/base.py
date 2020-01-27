#!/usr/bin/python3
'''Base class'''


import json
import os


class Base:
    '''This class will be the “base” of other subclasses in this project'''

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
                JSON_string_repr = []
                for obj in list_objs:
                    JSON_string_repr.append(obj.to_dictionary())
                my_list = f.write(Base.to_json_string(JSON_string_repr))
            return my_list

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        new_list = []
        try:
            with open(str(cls.__name__) + ".json", encoding='utf-8') as f:
                text = cls.from_json_string(f.read())
        except IOError:
            return new_list
        for char in text:
            new_list.append(cls.create(**char))
        return new_list
