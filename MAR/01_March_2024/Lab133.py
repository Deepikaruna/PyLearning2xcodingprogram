# File Handling
# How to Read a text, and Write into it using Python code

# Which function we need to use to read a file
#open("File name")

# Mode - What mode we need to use to read a file
# 'r' for reading(default)
# 'w' for writing(create a new file or truncates existing one)
# 'a' for appending
# 'b' for binary mode(Example .exe files)
# '+' for updating(Reading and writing)

# Read and write content
# Read a file
# Reading Entire content: content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for all lines in a list

# close the file

file = open("TestData.txt", 'r')
content = file.read()
print(content)
file.close()