#Multiple assignment with dictionaries

#To do this, we first make a list of tuples where each tuple is (value, key). The items method would give us a list of (key, value) tuples, but this time we want to sort by value, not key. Once we have constructed the list with the value-key tuples, it is a simple matter to sort the list in reverse order and print out the new, sorted list.

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
    l.append( (val, key) )

l
#[(10, 'a'), (22, 'c'), (1, 'b')]
l.sort(reverse=True)
l


#[(22, 'c'), (10, 'a'), (1, 'b')]
