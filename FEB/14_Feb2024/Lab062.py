# Lambda express
# It is used to convert any f(n) function to one liner in python

def say_hello():
    print("Hello")


say_hello()

# def double_my_salary(salary):
#   return salary*2
# result = double_my_salary(10000)
# print(result)

# to convert lambda express
d_salary = lambda salary: salary * 2
print(d_salary(10))

pow_of_two = lambda num: num ** 2
print(pow_of_two(16))

sum = lambda a,b:a+b
print(sum(3, 4))

say_my_name = lambda name : print("Your name is ", name)
say_my_name('Deepika')