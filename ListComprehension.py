my_string = 'hello'

# A way to initialise a list by appending it.
my_first_list = []

for letter in my_string:
    my_first_list.append(letter)

# Alternatively, we can comprehend the list to shorten the code
my_second_list = [letter for letter in 'Hello World']

print('First List: {} \nSecond List: {}'.format(my_first_list, my_second_list))

# List of squares
squares = [number ** 2 for number in range(0, 11)]
print('Squares: {}'.format(squares))

# List of even numbers upto 10
even_numbers = [numbers for numbers in range(0, 11) if numbers % 2 == 0]
print(f'Even Numbers: {even_numbers}')

# Temperature Conversion
celcius = [0, 10, 20, 32.5]
fehrenheit = [((9/5) * temperature + 32) for temperature in celcius]
print(f'Fehrenheit: {fehrenheit}')

# If-Else in list comprehension
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print('Result: {}'.format(results))