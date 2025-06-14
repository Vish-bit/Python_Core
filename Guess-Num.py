# Make a game where the  computer generates a random number, and the player has to guess it.
import random

random_num = random.randint(0, 10)
guess = None

while guess != random_num:
    guess = int(input('Enter your guess: '))  

    if guess < random_num:
        print('Too low! Try again.')
    elif guess > random_num:
        print('Too high! Try again.')
    else:
        print('Correct! You guessed the number.')
    