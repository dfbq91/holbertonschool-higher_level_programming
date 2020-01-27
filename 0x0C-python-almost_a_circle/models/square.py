#!/usr/bin/python3
'''Square subclass'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square as a subclass of Rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''init values for square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''returns [Square] (<id>) <x>/<y> - <size>'''
        x = self.x
        y = self.y
        s = self.width
        return "[Square] ({}) {}/{} - {}".format(self.id, x, y, s)

    @property
    def size(self):
        '''Returns size value assigned to an object'''
        return self.width

    @size.setter
    def size(self, value):
        '''Assign size value to an object'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute: id, size, x and y'''
        if args is not None and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''return a dic with attributes'''
        new_dict = {'id': self.id, 'x': self.x, 'size': self.size,
                    'y': self.y}
        return new_dict
