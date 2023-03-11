#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print('0')
if len(sys.argv) == 2:
    print('{}'.format(sys.argv[1]))
if len(sys.argv) >= 3:
    ans = int(sys.argv[1])
    for i in range(2, len(sys.argv)):
        ans = ans + int(sys.argv[i])
    print('{}'.format(ans))
