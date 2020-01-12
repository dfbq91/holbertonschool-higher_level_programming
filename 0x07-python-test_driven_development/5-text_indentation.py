#!/usr/bin/python3
'''Script to print a text with a behavior with some chracters'''


def text_indentation(text):
    '''Prints a text with 2 lines after each of these characters: ., ? and :'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        print(i, end='')
        if i == '.' or i == '?' or i == ':':
            print()
            print()
