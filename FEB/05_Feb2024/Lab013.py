# Strings--> Bunch of characters which can be represented by ' or ".

name1 = 'Deepika'
name2 = "Deepika"
print(name2)
print(type(name2))

dir = "C:\\abc\\abc.txt"
print(dir)

dir = "C:\\somedir\some dir"
print(dir)

#r --> Raw string ( This will be helpful in the directory paths)
dir = r"C:\\abc\\abc.txt"
print(dir)

#format string f
first_name = "Deepika"
last_name = " Kanu"
print(f"your name is {first_name}{last_name}")