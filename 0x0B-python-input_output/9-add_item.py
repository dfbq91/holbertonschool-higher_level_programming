#!/usr/bin/python3
'''adds all arguments to a Python list, and then save them to a file'''

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
my_list = []

try:
    my_list = load_from_json_file("add_item.json")
    for argument in sys.argv[1:]:
        my_list.append(argument)
    save_to_json_file(my_list, filename)
except:
    save_to_json_file(my_list, filename)
