#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as file1:
        nchars = file1.write(text)
        return nchars
