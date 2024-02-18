def say_hello_args(name, age):
    print("Hello", name, age)


say_hello_args("Deepika", 45)
say_hello_args(123, True)


def say_hello_args_default(name="kanudeep"):
    print("Hello", name)


say_hello_args_default()


def sum_number_argument_ret(a, b):
    return a + b


result = sum_number_argument_ret(3, 4)
result2 = sum_number_argument_ret("Deepika", "Kanu")
result3 = sum_number_argument_ret(a=10, b=90)
print(result)
print(result2)
print(result3)
