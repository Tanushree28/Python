#While this is a dysfunctional infinite loop, we can still use this pattern to build useful loops as long as we carefully add code to the body of the loop to explicitly exit the loop using break when we have reached the exit condition.

#For example, suppose you want to take input from the user until they type done. You could write:

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')