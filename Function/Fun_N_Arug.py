#Parameters and arguments
#Some of the built-in functions we have seen require arguments. For example, when you call math.sin you pass a number as an argument. Some functions take more than one argument: math.pow takes two, the base and the exponent.

def print_twice(bruce):
    print(bruce)
    print(bruce)
#This function works with any value that can be printed.

print_twice('Spam')
#Spam
#Spam

print_twice(17)
#17
#17

import math
print_twice(math.pi)
#3.141592653589793
#3.141592653589793