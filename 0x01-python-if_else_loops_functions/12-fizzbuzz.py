#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('{0: <9}'.format('FizzBuzz'), end="")
        elif i % 3 == 0:
            print('{0: <5}'.format('Fizz'), end="")
        elif i % 5 == 0:
            print('{0: <5}'.format('Buzz'), end="")
        elif i < 10:
            print('{0: <2}'.format(i), end="")
        elif i < 100:
            print('{0: <3}'.format(i), end="")
        else:
            print(i)
