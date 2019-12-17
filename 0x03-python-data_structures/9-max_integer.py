#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        bignum = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > bignum:
                bignum = my_list[i]
        return (bignum)
    else:
        return None
