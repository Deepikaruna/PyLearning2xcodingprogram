# Tuple - Collection of items. immutable
# like list - collection of items, list are mutable in nature

my_list = [1, 2, 3, 4, 5]
my_list[0] = 21
print(my_list)
print(type(my_list))

# Tuple - Another type of datatype and we cannot change values and immutable

my_tuple = (1, 2, 3, 4, 5)
# my_tuple(0) = 21 #Type error: 'Tuple'
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

# can we convert list to tuple, yes we can
new_tup = tuple(my_list)
print(new_tup)

