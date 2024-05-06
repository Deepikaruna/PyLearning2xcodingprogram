# list
# list - Collection of items(Duplicate is allowed)]

my_list = [1, 2, 3, 4, "True", 12.34]

#indexing
print("Element at index 0:", my_list[0])

# changing an element
my_list[1] = 20
print("list after changing the index 1", my_list)

# append
my_list.append(4)
print("List after appending:", my_list)

# extend
my_list.extend([5.6])
print("List after extending:", my_list)

# inserting
my_list.insert(1, 'a')
print("List after inserting 'a' at index:1", my_list)

# remove
my_list.remove('a')
print("List after removing 'a':", my_list)

# clear
my_copy_list = my_list.copy()
print(my_copy_list)

my_list.clear()
print("Initial list:", my_list)
print(my_copy_list)
