#!/usr/bin/python3
def islower(c):
    char = ord(c)
    if char >= 65 and char <= 90:
        return False
    elif char >= 97 and char <= 123:
        return True
