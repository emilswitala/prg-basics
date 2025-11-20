###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1,100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Test your luck & enter your guess!: "))

    if user_guess < number_to_guess:
        print("Too low! Don't give up!")
    elif user_guess > number_to_guess:
        print("Too high! Don't give up!")
    else:
        print("Ding, ding, ding!!! Right on the money!")