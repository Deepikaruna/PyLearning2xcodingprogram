# Triangle Cla

# side1 == side2 == side3  --> Equilateral triangle
# side1 == side2 or side2 == side3 or side1 == side3 --> Isolate triangle
# else --> scalene triangle

side1 = float(input("Enter the side1\n"))
side2 = float(input("Enter the side2\n"))
side3 = float(input("Enter the side3\n"))

if side1 == side2 == side3:
    print("EQ")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Iso")
else:
    print("scalene triangle")