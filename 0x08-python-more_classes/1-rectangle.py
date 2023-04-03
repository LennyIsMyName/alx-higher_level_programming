#!/usr/bin/python3
""" create a class called rectangle """


class Rectangle:
    """ the rectangle class """
    def __init__(self, width=0, height=0):
#        if not isinstance(width, int):
#            raise TypeError("width must an integer")
#        elif width < 0:
#            raise ValueError("width must be >= 0")
#        else:
            self.__width = width

#        if not isinstance(height, int):
#            raise TypeError("height must an integer")
#        elif height < 0:
#            raise ValueError("height must be >= 0")
#        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
