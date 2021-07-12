import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number = 100000))

stmt1 = '''
func_two(100)
'''

setup1 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt1, setup1, number = 100000))