#!/usr/bin/python3
def number_of_lines(filename=""):
    nlines = 0
    with open(filename, encoding='utf-8') as file1:
        for line in file1:
            nlines += 1
    return nlines
