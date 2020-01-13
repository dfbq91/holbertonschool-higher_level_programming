#!/usr/bin/python3
'''Script to print a text with a behavior with some chracters'''


def text_indentation(text):
    '''Prints a text with a space after each of these characters: ., ? and :'''
    flag = 1

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i == ' ' and flag == 0:
            continue
        else:
            flag = 1
            print(i, end='')
        if i == '.' or i == '?' or i == ':':
            flag = 0
            print()
            print()
    print()
