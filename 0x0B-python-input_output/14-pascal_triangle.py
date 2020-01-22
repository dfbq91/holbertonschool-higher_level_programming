#!/usr/bin/python3
def pascal_triangle(n):
    lista = []
    if n <= 0:
        return lista
    else:
        number1 = 1
        new_number = 0
        for i in range(0, n - 1):
            if n == 1:
                return(lista.append([number1]))
            if n == 2:
                return(lista.append([number1, number1]))
            else:
                lista.append([number1, 
