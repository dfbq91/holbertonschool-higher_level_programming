#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    nlines = 0
    with open(filename, encoding='utf-8') as file1:
        for line in file1:
            nlines += 1
    with open(filename, encoding='utf-8') as file1:
        if nb_lines <= 0 or nb_lines > nlines:
            lines_readed = file1.read()
            print(lines_readed)
        else:
            lines_printed = 0
            for lines in file1:
                if lines_printed == nb_lines:
                    break
                print(lines, end='')
                lines_printed += 1
