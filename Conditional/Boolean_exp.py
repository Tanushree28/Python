#Boolean expressions
#A boolean expression is an expression that is either true or false. The following examples use the operator ==, which compares two operands and produces True if they are equal and False otherwise:

5 == 5
#True


5 == 6
#False


#True and False are special values that belong to the class bool; they are not strings:

type(True)
#<class 'bool'>

type(False)
#<class 'bool'>

#The == operator is one of the comparison operators; the others are:

#x != y               # x is not equal to y
#x > y                # x is greater than y
#x < y                # x is less than y
#x >= y               # x is greater than or equal to y
#x <= y               # x is less than or equal to y
#x is y               # x is the same as y
#x is not y           # x is not the same as y