#!/usr/bin/python3
import sys
if __name__ == "__main__":
    j = 1
    suma = 0

    if len(sys.argv) == 1:
        print("{:d}".format(0))
    elif len(sys.argv) > 1:
        for i in sys.argv[1:]:
            suma = suma + int(sys.argv[j])
            j = j + 1
        print("{}".format(suma))
