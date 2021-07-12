from random import randint

number = randint(1, 100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\nWhat is your guess?"))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess == number:
        print(f'CONGRATULATIONS, You guessed it only in {len(guesses)} guesses!!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(number - guess) < abs(number - guesses[-2]):
            print('Warmer')
        else:
            print('Colder')

    else:
        if abs(number - guess) <= 10:
            print('Warm')
        else:
            print('Cold')