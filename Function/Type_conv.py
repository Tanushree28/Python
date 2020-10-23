#Type conversion functions


#Python also provides built-in functions that convert values from one type to another. The int


#int can convert floating-point values to integers, but it doesn’t round off; it chops off the fraction part:

int(3.99999)
#3

int(-2.3)
#-2


#float converts integers and strings to floating-point numbers:

float(32)
#32.0

float('3.14159')
#3.14159



#Finally, str converts its argument to a string:

str(32)
#'32'

str(3.14159)
#'3.14159'