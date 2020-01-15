#!/usr/bin/python3
'''Module that creates a new class with
width and height, also area, perimeter,
del, str and repr methods defined'''


class Rectangle:
    '''Class with width and height'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''init values for an object of rectangle class'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Returns width value assign to an object(rectangle)'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Assign a value to a width of object(rectangle)'''
        if type(value) is int and value >= 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''Returns height value assign to an object(rectangle)'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int and value >= 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''Returns the object(rectangle) area'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns the perimeter of object(rectangle)'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        '''Print the rectangle using #'''
        rect_print = ""
        if self.__width == 0 or self.__height == 0:
            return rec_print
        for y in range(self.__height):
            for x in range(self.__width):
                rect_print += str(self.print_symbol)
            if x == self.__width - 1 and y != self.__height - 1:
                rect_print += "\n"
        return rect_print

    def __repr__(self):
        '''return a string representation of the rectangle
        to be able to recreate a new instance by using eval()'''
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        '''Delete an object(rectangle)'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif int(rect_1.area()) >= int(rect_2.area()):
            return rect_1
        elif int(rect_1.area()) < int(rect_2.area()):
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''
        return Rectangle(size, size)
