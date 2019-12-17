#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        listcopy = my_list.copy()
        for i in range(len(listcopy)):
            if listcopy[i] % 2 == 0:
                listcopy[i] = True
            else:
                listcopy[i] = False
        return listcopy
