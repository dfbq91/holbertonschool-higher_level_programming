#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        newlist = []
        newlist = [replace if x == search else x for x in my_list]
        return newlist
