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
            self.__width = value

    def update(self, *args, **kwargs):
        """ update the values """
        li = [self.id, self.__width, self.__height, self.__x, self.__y]

        le = len(args)

        if le == 1:
            self.id = args[0]
        if le == 2:
            self.id = args[0]
            self.__width = args[1]
        if le == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        if le == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        if le == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

        if le == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
