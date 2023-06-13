#!/usr/bin/python3

""" this program creates an empty class """


class BaseGeometry():
    """
    creates an empty class
    improvement.. raise exception
    """
    def area(self):
        """
        just raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(self.value, int):
            raise TypeError(f"{name} must be an integer")
        if self.value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value

if __name__ == "__main__":
    import doctest
    doctest.testfile("test/7-base_geometry.txt")

