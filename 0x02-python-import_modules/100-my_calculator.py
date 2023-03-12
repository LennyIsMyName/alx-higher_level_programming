#!/usr/bin/python3
# make use of calculator_1.py
import sys
from calculator_1 import sub, mul, div, add

if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = sys.argv[2]

    if sign != '*' or sign != '/' or sign != '+' or sign != '-':
        print("Unknown operator. Available operators: +, -, * and /")
        return (1)
    if sys.argv[2] == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif sys.argv[2] == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
