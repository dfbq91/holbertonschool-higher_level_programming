#!/usr/bin/python3
'''Square class with a size and a position'''


class Square():
    '''Square class with size and position'''

    def __init__(self, size=0, position=(0, 0)):
        '''Init values for a square'''
        self.size = size
        self.position = position

    def area(self):
        '''Return area of the square'''
        return self.__size * self.__size

    @property
    def size(self):
        '''Return size of the square'''
        return self.__size

    def my_print(self):
        '''Print square from a given position'''
        for y in range(self.position[1]):
            print()
        if self.__size == 0:
            print()
        for i in range(self.size):
            for x in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        '''Assign value as a size of the square'''
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        '''Asiggn position from the square will be printed'''
        if type(value) == tuple and len(value) == 2 and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
