#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        newlist = []
        for i in range(len(matrix)):
            newlist.append(list(map(lambda x: x ** 2, matrix[i])))
        return newlist
