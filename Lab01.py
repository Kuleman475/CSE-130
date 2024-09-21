# 1. Name: 
#    Taylor Christensen
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Make a number guessing game that gives hints to help you find the number.
# 4. What was the hardest part? Be as specific as possible.
#    the hardest part for me was trying to figure out how to have the while statement
# 5. How long did it take for you to complete the assignment?
#    about an hour  

import random

# Game introduction.
print('This is the "guess a number" game.')
# Give the user instructions as to what he or she will be doing.
print('You try to guess a random number in the smallest number of attempts.')


# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Please input a positive integer: "))
print(f"Pick a number between 1 and {value_max}")
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Initialize the sentinal and the array of guesses.
numGusses = []
# Play the guessing game.
guess = int(input("> "))
count = 1

while guess != value_random:
    count += 1
    numGusses.append(guess)
    if guess > value_random:
        print("         Too High")
    else:
        print("         Too Low")    
    guess = int(input("> "))
    

    # Prompt the user for a number.

    # Store the number in an array so it can be displayed later.

    # Make a decision: was the guess too high, too low, or just right.
numGusses.append(guess)
print(f"Congratulations you have guessed the number in {count} guesses")
print(f"The number you have guessed {numGusses}")
# Give the user a report: How many guesses and what the guesses where.
