#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newdic = a_dictionary.copy()
    [print(key, ":", value) for (key, value) in sorted(newdic.items())]
