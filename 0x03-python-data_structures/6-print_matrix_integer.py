#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            t = 0
            for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end=''),
                t = t + 1
                if t != len(matrix[i]):
                    print(" ", end='')
            print()
