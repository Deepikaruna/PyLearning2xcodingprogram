# Factorial
# fibanoci series
# default = 1

# Reverse a string

str = "Karuna"
rev_str = ""
for c in str:
    rev_str = c + rev_str
print(rev_str)


# palindrome - str = rev_str --> p

def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str

original_str = input("Enter the string\n")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str :
    print("palindrome")
else:
    print("Not a palindrome")
