#!/usr/bin/python3
# print list of ints in reversed order
def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(len(my_list))):
        print('{}'.format(my_list[i]))
