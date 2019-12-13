#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    first = int(sys.argv[1])
    second = int(sys.argv[3])
    op = sys.argv[2]

    if sys.argv[2] == '+':
        print("{} {} {} = {}".format(first, op, second, add(first, second)))

    elif sys.argv[2] == '-':
        print("{} {} {} = {}".format(first, op, second, sub(first, second)))

    elif sys.argv[2] == '*':
        print("{} {} {} = {}".format(first, op, second, mul(first, second)))

    elif sys.argv[2] == '/':
        print("{} {} {} = {}".format(first, op, second, div(first, second)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
