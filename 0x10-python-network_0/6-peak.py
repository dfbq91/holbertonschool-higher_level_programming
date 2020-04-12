#!/usr/bin/python3
# peak element


def find_peak(list_of_integers):
    '''find a peak element'''

    # No elements
    if len(list_of_integers) == 0:
        return None
    # Just 1 element
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    # Two elements
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers)//2

    # check if mid is a peak
    if list_of_integers[mid] > list_of_integers[mid - 1] and \
       list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]

    # go right
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[0:mid])

    # go left
    else:
        return find_peak(list_of_integers[mid + 1:])
