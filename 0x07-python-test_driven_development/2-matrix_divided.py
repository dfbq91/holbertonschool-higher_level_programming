#!/usr/bin/python3
'''Script to dive elements of a matrix(list)'''


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix'''
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(msg1)

    for checkrow in matrix:
        if type(checkrow) is not list:
            raise TypeError(msg1)

    for checkrow in matrix:
        if len(checkrow) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    for i in matrix:
        for j in i:
            if type(j) == int or type(j) == float:
                continue
            else:
                raise TypeError(msg1)

    for i in matrix:
        new_matrix.append([round((j / div), 2) for j in i])

    return new_matrix
