# *args and **kargs
# *args
def sum(a, b, c):
    return a + b + c


r = sum(1, 2, 3)
print(r)


def print_arguments(*args):
    for i in args:
        print(i, end= "  ")


print_arguments(1)
print_arguments(1, 2)
print_arguments(1, 2, 3)
