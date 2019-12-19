#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    for key in newdic:
        newdic[key] *= 2
    return newdic
