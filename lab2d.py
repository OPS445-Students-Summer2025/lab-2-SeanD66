#!/usr/bin/env python3


import sys


#name = sys.argv[1]
#age = sys.argv[2]

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2] 

result = 'Hi ' + name + ', you are ' + str(age) + ' years old.'

print(result)


