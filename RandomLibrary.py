from random import shuffle, randint

# Creating a list and then shuffling it
mylist = list(range(1, 11))
shuffle(mylist)

# Assigning a random value to a variable in range [1, 100] (including both points)
mynumber = randint(1, 100)

print(f'List: {mylist}')
print(f'Random Integer: {mynumber}')