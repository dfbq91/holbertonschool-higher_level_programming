#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print(key, ":", value) for (key, value) in sorted(a_dictionary.items())]
