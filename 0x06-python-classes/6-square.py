#!/usr/bin/python3

""" size validation of Square"""

class Square:
    """ The square class """

    def __init__(self, size=0, position=(0, 0)):
        """ init a new square class. 
        Args:
            size (int): size to validate.
            position (tuple): x,y
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
    @property
    def position(self):
        """ get att """
        return position
    
    @position.setter
    def position(self, value):
        """set att """
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            
    @property
    def size(self):
        """ get att """
        return self.__size

    @size.setter
    def size(self, value):
        """ set att """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the current square"""
        var = self.__size * self.__size
        return var

    def my_print(self):
        """ prints a square of # characters """
        if self.__size:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='') 
                print()
        elif self.__size == 0:
            print()
