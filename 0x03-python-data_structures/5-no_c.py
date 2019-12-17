#!/usr/bin/python3
def no_c(my_string):
    newlist = list(my_string)
    for i in newlist:
        try:
            upperletter = newlist.index('c')
        except ValueError:
            upperletter = -1
        try:
            lowerletter = newlist.index('C')
        except ValueError:
            lowerletter = -1

        if upperletter != -1:
            newlist.pop(upperletter)
        if lowerletter != -1:
            newlist.pop(lowerletter)

    newnewlist = ''.join(newlist)
    return newnewlist
