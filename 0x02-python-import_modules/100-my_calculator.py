#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    first = int(sys.argv[1])
    second = int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{} + {} = {}".format(first, second, add(first, second)))

    elif sys.argv[2] == '-':
        print("{} - {} = {}".format(first, second, sub(first, second)))

    elif sys.argv[2] == '*':
        print("{} * {} = {}".format(first, second, mul(first, second)))

    elif sys.argv[2] == '/':
        print("{} / {} = {}".format(first, second, div(first, second)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
