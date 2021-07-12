# Question 1
st = 'Print only the words that start with s in this sentence'

print('\nWords start with S...')

for word in st.split():
    if word[0].lower() == 's':
        print(word)

# Question 2
even_numbers = list(range(0, 11, 2))
print('\nList of even numbers: {}'.format(even_numbers))

# Question 3
numbers_divisible_by_3 = [number for number in range(1, 51) if number % 3 == 0]
print(f'\nNumbers divisible by 3: {numbers_divisible_by_3}')

# Question 4
st = 'Print every word in this sentence that has an even number of letters'

print('\nEven word length...')

for word in st.split():

    if len(word) % 2 == 0:
        print('even!')
    else:
        print(word)

# Question 5
print('\nFizzBuzz Program...')

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')

    elif number % 3 == 0:
        print('Fizz')

    elif number % 5 == 0:
        print('Buzz')

    else:
        print(number)

# Question 6
st = 'Create a list of the first letters of every word in this string'

my_list = [word[0] for word in st.split()]

print('\nList: {}'.format(my_list))
