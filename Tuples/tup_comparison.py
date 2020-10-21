#Comparing tuples
#The comparison operators work with tuples and other sequences. Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next element, and so on, until it finds elements that differ. Subsequent elements are not considered (even if they are really big).

(0, 1, 2) < (0, 3, 4)
#True



(0, 1, 2000000) < (0, 3, 4)
#True