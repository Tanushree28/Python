#if statements have the same structure as function definitions or for loops1. The statement consists of a header line that ends with the colon character (:) followed by an indented block. Statements like this are called compound statements because they stretch across more than one line.

#There is no limit on the number of statements that can appear in the body, but there must be at least one. Occasionally, it is useful to have a body with no statements (usually as a place holder for code you haven’t written yet). In that case, you can use the pass statement, which does nothing.


x = 3
if x < 10:
    print('Small')
...
#Small