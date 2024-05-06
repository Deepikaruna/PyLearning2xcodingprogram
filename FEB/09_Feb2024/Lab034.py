# problem Find the maximum between 3 numbers

num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

max_number = max(num1,num2,num3)
print(max_number)

if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("Max is", num3)
