#!/usr/bin/python3

def uppercase(str):
    for i in str:
         print("{}".format(chr(ord(i) - 32) if (ord(i) >= 97 and ord(i) <= 122) else i), end='')
    print("{}".format(''))



'''

    if ord(i) >= 97 and ord(i) <= 122:
        print(chr(ord(i) - 32), end="")
    else:
        print("{}".format(i), end="")
    print()
'''
