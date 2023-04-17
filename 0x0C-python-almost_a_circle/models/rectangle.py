#!/usr/bin/python3

""" inherit base to rectangle """
##from base import Base
from models.base import Base

class Rectangle(Base):
    """ the rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle constructor """
        if not isinstance(width, int):
            raise TypeError("width must be integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)
    
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value 

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value 

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value 

    def area(self):
        return self.__width * self.__height

    def display(self):
        """ display the rectangle """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print('#', end="")
            print()
        print()

    def __str__(self):
        """ overwrite the __str__ method """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

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
