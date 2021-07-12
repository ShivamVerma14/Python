# Example of nested function
def hello(name = 'Shivam'):
    print('This is hello() function.')

    def greet():
        return '\tThis is greet() function inside hello.'

    def welcome():
        return '\tThis is welcome() function inside hello.'

    print('Now, we will return a function.')

    if name == 'Shivam':
        return greet
    else:
        return welcome


def hi():
    return 'Hello Shivam'

def other(hola):
    print('This will execute more code.')
    print(hola())

# This will assign the returning function to this name
# So, we can call the returned function with this new name
my_new_func = hello()
print(my_new_func())

other(hi)