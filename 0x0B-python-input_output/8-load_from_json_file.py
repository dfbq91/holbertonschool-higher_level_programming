#!/usr/bin/python3
'''json tasks'''


import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file'''
    with open(filename, 'r', encoding='utf-8') as file1:
        return json.load(file1)
