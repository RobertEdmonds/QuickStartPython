"""This is the build for a number guessing game"""
# from random import seed
from random import randint
# create an answer for the loop
number = randint(10, 100)
# create an input for the user to guess
guess = int(input("What is your guess between 10 and 100: "))
# need to create a loop
    # it will check to see if the two numbers match
while guess != number:
    if guess > number:
        print("You were to high!")
    else:
        print("You were to low!")
    hint = input("Would you like a hint? ")
    if hint == "Yes":
        amount = 0
        if guess > number:
            amount = guess - number
        else:
            amount = number - guess
        print(f"You were off by {amount}")
        guess = input("Sorry that is incorrect. Try again: ")
    else:
        guess = input("Sorry that is incorrect. Try again: ")
    if guess == "No":
        print("Sorry that you suck!")
        break
    else:
        guess = int(guess)
        # if they do they will print you guessed right
        # if not it will let you guess again
else:
    print("You are the winner!")
     