#!/usr/bin/python3

def print_last_digit(number):
    number = abs(int(number))
    print("{}".format(number % 10), end="")
