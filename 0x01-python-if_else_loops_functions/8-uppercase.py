#!/usr/bin/python

def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(i) - 32) if (ord(i) >= 97 and ord(i) <= 122) else i), end='')
    print()


'''
        if ord(i) >= 97 and ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
'''
