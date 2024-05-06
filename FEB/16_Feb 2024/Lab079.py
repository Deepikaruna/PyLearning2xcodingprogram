t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(t))

# you can also do union in sets. it means all the items between set1 and set2
set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_Set = set1.union(set2)
print(my_Set)

# intersection in sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_Set = set1.intersection(set2)
print(my_Set)

# difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_Set = set1.difference(set2)
print(my_Set)
