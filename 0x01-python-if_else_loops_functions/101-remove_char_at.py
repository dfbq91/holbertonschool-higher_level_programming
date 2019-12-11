#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str1 = str[0:n]
        str2 = str[n + 1:]
        return(str1 + str2)
    return(str)
