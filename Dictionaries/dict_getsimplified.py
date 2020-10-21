#we can use get() and provide a default value of zero when the key is not yet in the dictionary.

counts = dict()
names = ['csev','cwen','qwer','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)