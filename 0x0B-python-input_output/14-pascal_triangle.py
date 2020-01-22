#!/usr/bin/python3
'''pascal triangle'''

def pascal_triangle(n):
    ''' returns a list of lists of integers
    representing the Pascal’s triangle of n:'''
    result = []
    if n <= 0:
        return result
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result
