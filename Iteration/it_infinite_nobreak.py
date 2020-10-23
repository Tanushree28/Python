#The while statement
#Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly. Because iteration is so common, Python provides several language features to make it easier.

#One form of iteration in Python is the while statement. Here is a simple program that counts down from five and then says “Blastoff!”.

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')