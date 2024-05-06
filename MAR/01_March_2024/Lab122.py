# Handle exception
# try and except block
#try - try the code
# except - execute the except code if there is problem in try

a = int(input("Enter num 1\n"))
b = int(input("Enter num 2\n"))

try:
    c = a/b    #ZeroDivisionError: division by zero
    print("Div is ", c)
except Exception as e:
    print(e)
    print("Zero Division, Please dont use B as Zero!")

print("This is important message that we need to show to user")







