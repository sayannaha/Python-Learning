#Find the intersection (common) of two sets and remove those elements from the Sets
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print("First Set ", first_set)
print("Second Set ", second_set)
intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)
    second_set.remove(item)
print("First Set after removing common element ", first_set)
print("Second Set after removing common element ", second_set)