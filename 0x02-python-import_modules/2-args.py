#!/usr/bin/python3
import sys
# print command line arguments and their positions
num = len(sys.argv)
if num == 1:
    print('{} arguments.'.format(num - 1))
elif num == 2:
    print('{} argument:'.format(num - 1))
    print('{}: {}'.format(1, sys.argv[1]))
else:
    print('{} arguments:'.format(num - 1))
    for i in range(1, num):
        print('{}: {}'.format(i, sys.argv[i]))

