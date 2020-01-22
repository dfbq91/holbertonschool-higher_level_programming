#!/usr/bin/python3
'''read task'''


def read_file(filename=""):
    '''read a file and prints it to stdout'''
    with open(filename, encoding='utf-8') as file1:
        print(file1.read(), end="")
