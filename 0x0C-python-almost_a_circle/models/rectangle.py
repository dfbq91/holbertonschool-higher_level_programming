#!/usr/bin/python3
'''Rectangle subclass'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle as a subclass of Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

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
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int and value >= 0:
            self.__x = value
        elif type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int and value >= 0:
            self.__y = value
        elif type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''returns the area value of the Rectangle instance'''
        return self.__width * self.__height

    def display(self):
        '''prints the Rectangle instance with (x, y) position #'''
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(''.join(' ' for x in range(self.__x)), end='')
            print(''.join('#' for j in range(self.__width)), end='')
            print()

    def __str__(self):
        '''returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, x, y, w, h))

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute: id, width, height, x and y'''
        if args is not None and args != ():
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns a dictionary representaton of rectangle'''
        new_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                    'height': self.__height, 'width': self.__width}
        return new_dict
