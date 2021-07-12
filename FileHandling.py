# Opens the file
# file = open('myfile.txt')

# Reads the file and returns the string
# file.seek(0)
# print(file.read())

# Reads the file and returns the list containing each line
# file.seek(0)
# print(file.readlines())

# Closes the file
# file.close()

# Alternatively we can open files without worrying about closing it
# with open('myfile.txt') as file:
#     contents = file.read()
#     print(contents)

# Opens the file in append mode
with open('myfile.txt', mode = 'a') as file:
    file.write('\nThis is the fourth line')

with open('myfile.txt') as file:
    print(file.read())