#!/usr/bin/python3
for i in range(00, 10):
    if i < 10:
        print("0{}".format(i), end=', ')
print(*range(10, 100), sep=", ")
