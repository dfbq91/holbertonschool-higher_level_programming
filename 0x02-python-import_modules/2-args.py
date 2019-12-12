#!/usr/bin/python3
import sys
j = 1
if __name__ == "__main__":
    lent = len(sys.argv) - 1

    if lent == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif lent == 1:
        print("{} argument:".format(len(sys.argv) - 1))
    elif lent == 2:
        print("{} arguments:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in sys.argv[1:]:
          print("{}: {}".format(j, sys.argv[j]))
          j = j + 1
