#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i == j or i > j:
            continue
        if (i != 8):
            print("{}{}, ".format(i, j), end='')
        if i == 8:
            print("{}{} ".format(i, j), sep='')
