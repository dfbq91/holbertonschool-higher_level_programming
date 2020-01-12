#!/usr/bin/python3
'''Script to dive elements of a matrix(list)'''


def matrix_divided(matrix, div):
    '''function that divides all elements of a matrix'''
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[]]

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"

    for i in range(0, len(matrix) + 1):
        for j in matrix[i]:
            if type(j) == int or type(j) == float:
                new_matrix.append(j / div)
        else:
            raise TypeError(msg1)


        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

        if type(div) != int or type(div) != float:
            raise TypeError("div must be a number")
