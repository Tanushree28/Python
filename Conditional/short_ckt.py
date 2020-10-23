#Short-circuit evaluation of logical expressions
#When Python is processing a logical expression such as x >= 2 and (x/y) > 2, it evaluates the expression from left to right. Because of the definition of and, if x is less than 2, the expression x >= 2 is False and so the whole expression is False regardless of whether (x/y) > 2 evaluates to True or False.

#When Python detects that there is nothing to be gained by evaluating the rest of a logical expression, it stops its evaluation and does not do the computations in the rest of the logical expression. When the evaluation of a logical expression stops because the overall value is already known, it is called short-circuiting the evaluation.

#While this may seem like a fine point, the short-circuit behavior leads to a clever technique called the guardian pattern. Consider the following code sequence in the Python interpreter:

x = 6
y = 2
x >= 2 and (x/y) > 2
#True
x = 1
y = 0
x >= 2 and (x/y) > 2
#False
x = 6
y = 0
x >= 2 and (x/y) > 2

#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#ZeroDivisionError: division by zero
#>>>