#Dictionaries and tuples
#Dictionaries have a method called items that returns a list of tuples, where each tuple is a key-value pair:

d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
print(t)


#[('b', 1), ('a', 10), ('c', 22)]
