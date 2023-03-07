#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ten = 10
last = abs(number) % ten
a = "Last digit of"
if number < 0:
    last = -abs(last)

if last > 5:
    print("{} {} is {} and is greater than 5".format(a, number, last))
elif last == 0:
    print("{} {} is 0 and is 0".format(a, number))
elif last < 6 and not 0:
    print("{} {} is {} and is less than 6 and not 0".format(a, number, last))
