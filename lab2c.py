#!/usr/bin/env python3


import sys


#name = sys.argv[1]
#age = sys.argv[2]
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')


print(len(sys.argv))

if len(sys.argv) != 10:
    print('you do not have 10 arguments')
    sys.exit

