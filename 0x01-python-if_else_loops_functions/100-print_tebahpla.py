#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        j = i
    elif i % 2 != 0:
        j = i - 32
    print("{}".format(chr(j)), end='')
