#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        newlist = my_list.copy()
        for n, i in enumerate(newlist):
            if i == search:
                newlist[n] = replace
        return newlist
