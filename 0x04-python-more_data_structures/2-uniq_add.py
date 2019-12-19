#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = my_list.copy()
    return sum(set(newlist))
