#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    li = sorted(list(a_dictionary.keys()))

    for key in li:
        print('{}: {}'.format(key, a_dictionary[key]))
