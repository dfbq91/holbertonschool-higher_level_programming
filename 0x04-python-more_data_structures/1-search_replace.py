#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        newlist = my_list.copy()
        newlist = [replace if x == search else x for x in newlist]
        return newlist
