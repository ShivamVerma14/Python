def lesser_of_two_numbers(first_number, second_number):

    if first_number % 2 == 0 and second_number % 2 == 0:
        return min((first_number, second_number))

    else:
        return max((first_number, second_number))

def animal_crackers(text):
    return text.split()[0][0] == text.split()[1][0]

def makes_twenty(first_number, second_number):
    return first_number == 20 or second_number == 20 or first_number + second_number == 20

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return name.capitalize()

def master_yoda(text):
    return ' '.join(text.split()[::-1])

def almost_there(number):
    return abs(number - 100) <= 10 or abs(number - 200) <= 10

def has_33(nums):
    for index in range(0, len(nums) - 1):
        if nums[index] == 3 and nums[index + 1] == 3:
            return True
        
    return False

def paper_doll(text):
    letters = []

    for letter in text:
        letters.append(letter*3)

    return ''.join(letters)

def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10

    else:
        return 'BUST'

def summer_69(arr):
    total = 0
    index = 0

    while index < len(arr):

        if arr[index] != 6:
            total += arr[index]

        else:
            while arr[index] != 9:
                index += 1

        index += 1

    return total

def spy_game(nums):
    for index in range(0, len(nums) - 2):
        if nums[index] == 0 and nums[index + 1] == 0 and nums[index + 2] == 7:
            return True

    return False

def count_primes(num):
    prime_numbers = [2]
    x = 3

    if num < 2:
        return 0
    while x <= num:
        for y in prime_numbers:
            if x % y == 0:
                x += 2
                break

        else:
            prime_numbers.append(x)
            x += 2

    return len(prime_numbers)


print(count_primes(100))