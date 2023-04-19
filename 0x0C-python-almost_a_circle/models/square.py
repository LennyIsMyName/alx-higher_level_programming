#!/usr/bin/python3
""" create the square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ inherit the square class from the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize the square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overwrite the __str__ method """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width)

    @property
    def size(self):
        """ get the size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

        self.height = value

    def to_dictionary(self):
        """ returns a dict representation of this class """
        dic = {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
        return dic

    def update(self, *args, **kwargs):
        """ update the values """
        li = [self.id, self.size, self.x, self.y]

        le = len(args)

        if le == 1:
            self.id = args[0]
        if le == 2:
            self.id = args[0]
            self.size = args[1]
        if le == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        if le == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        if le == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
