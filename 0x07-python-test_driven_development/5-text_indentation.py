#!/usr/bin/python3
'''Script to print a text with a behavior with some chracters'''


def text_indentation(text):
    '''Prints a text with a space after each of these characters: ., ? and :'''
    flag = 1
    delimiters = ['?', '.', ':']

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        if char == ' ' and flag == 1:
            continue

        if char == '.' or char == '?' or char == ':':
            print("{}".format(char), end="")
            print("\n")
            flag = 1

        else:
            print(char, end="")
            flag = 0
