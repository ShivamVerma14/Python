# This function will create a list of cubes and returns it. But it is not memory efficient.
def create_cubes(num): 
    result = []

    for x in range(num):
        result.append(x ** 3)

    return result

# Therefore, generators are used as it keeps track of last number and will not generate a list
def cubes_generator(num):
    for x in range(num):
        yield x ** 3

# Generator function for Fibonacci Series
def fibonacci_generator(num):
    a, b = 0, 1
    for x in range(num):
        yield a
        a, b = b, a + b

# Normal Generator
def simple_generator():
    for number in range(3):
        yield number

print("Fibonacci Series...")
for x in fibonacci_generator(10):
    print(x)

print('\nNumbers...')
g = simple_generator()
print(next(g))
print(next(g))
print(next(g))


# iter() allows to iterate through normal objects 
s = 'hello'
s_iter = iter(s)
print('\nIter()...')
for i in range(5):
    print(next(s_iter))