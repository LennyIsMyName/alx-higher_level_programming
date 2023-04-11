#!/usr/bin/python3

""" Inherit from the builtin list class """

class MyList(list):
    """ inherits the list class and uses its method. """
    def print_sorted(self):
        """ Uses the sorted method of a list class."""
        newl = sorted(self) 
        print(newl)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/1-my_list.txt', package='1-my_list')
