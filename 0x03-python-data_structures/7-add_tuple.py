#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            newa = (tuple_a[0], 0)
        if len(tuple_a) == 0:
            newa = (0, 0)
    else:
        newa = (tuple_a[0], tuple_a[1])

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            newb = (tuple_b[0], 0)
        if len(tuple_b) == 0:
            newb = (0, 0)
    else:
        newb = (tuple_b[0], tuple_b[1])

    newt = (newa[0] + newb[0], newa[1] + newb[1])

    return newt
