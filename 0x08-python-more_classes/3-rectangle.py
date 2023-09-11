#!/usr/bin/python3
""" create a class called rectangle """


class Rectangle:
    """ the rectangle class """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("width must an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def printer(self):
        for i in range(self.__height):
            print("{}".format('#' * self.__width))
        
    def __repr__(self):
        return repr(self)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return self.printer()
