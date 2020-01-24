#!/usr/bin/python3
'''Square subclass'''


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square as a subclass of Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''returns [Square] (<id>) <x>/<y> - <size>'''
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({}) {}/{} - {}".format(self.id, x, y, size)

    @property
    def size(self):
        '''Returns size value assigned to an object'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Assign size value to an object'''
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute: id, size, x and y'''
        if args is not None and args != ():
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        new_dict = {'id': self.id, 'x': self.x, 'size': self.size,
                    'y': self.y}
        return new_dict
