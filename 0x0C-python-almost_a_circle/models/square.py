#!/usr/bin/python3
'''Square subclass'''


from models.base import Base
from models.Rectangle import Rectangle


class Square(Rectangle):
    '''Square as a subclass of Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, width, height, x, y)
        self.__size = size

    @property
    def width(self):
        '''Returns width value assign to an object'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Assign a value to a width of object'''
        if type(value) is int and value > 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError(value, " must be an integer")
        elif value <= 0:
            raise ValueError(value, " must be > 0")

    @property
    def height(self):
        '''Returns height value assign to an object'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Assign a value to a height of object'''
        if type(value) is int and value > 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError(value, " must be an integer")
        elif value <= 0:
            raise ValueError(value, " must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int and value >= 0:
            self.__x = value
        elif type(value) is not int:
            raise TypeError(value, " must be an integer")
        elif value < 0:
            raise ValueError(value, " must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int and value >= 0:
            self.__y = value
        elif type(value) is not int:
            raise TypeError(value, " must be an integer")
        elif value < 0:
            raise ValueError(value, " must be >= 0")

    def area(self):
        '''returns the area value of the Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''prints the Rectangle instance with (x, y) position #'''
        for y in range(self.__y):
            print()
        for i in range(self.__x + 1):
            print(''.join('.' for x in range(self.__x)), end='')
            print(''.join('#' for j in range(self.__width)), end='')
            print()

    def __str__(self):
        '''returns [Square] (<id>) <x>/<y> - <size>'''
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return ("[Square] ({}) {}/{} - {}".format(self.id, x, y, w))

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute: id, width, height, x and y'''
        if args is not None and args != ():
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
