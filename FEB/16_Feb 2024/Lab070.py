# filter
# It can filter the items from the list based on the logic
# return less number of items

number = [1,2,3,4,5,6]
even_numbers = filter(lambda x:x%2 == 0,number)
print(list(even_numbers))

def even(num):
    return num %2 == 0
even_lamba = lambda num:num%2 == 0