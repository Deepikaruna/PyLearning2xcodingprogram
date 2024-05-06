import math
def sq_rt(num):
    return math.sqrt(num)

#list,tuple,dictonary
my_list = [21, 34, 54]
sq_list = list(map(sq_rt, my_list))
print(sq_list)
