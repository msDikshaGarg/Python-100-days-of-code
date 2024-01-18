# Importing relevant libraries and files
import random
import os
from artwork import art

# Greeting function
def greeting():
    print(art)
    print("You are now playing the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

# Declaring global variables 
lives = 0
try_again = True

# Check if the guessed number is higher or lower than the actual number
def check_guess(num, guess):
    if num - guess < 0 and abs(num - guess) >= 10: 
        print("Too high!")
    elif num - guess < 0 and abs(num - guess) < 10: 
        print("Close but high!")
    elif num - guess >= 10:
        print("Too low!")
    else: 
        print("Close but low!")

# Ask the player if they want to play easy mode or hard mode
def select_level():
    level = input("What level will you play at today, easy or hard?\n").lower()
    while level not in ['hard', 'easy']:
        level = input("Please enter a valid input.\n").lower()
    if level == 'hard':
        lives = 5
        print("You have 5 lives.")
    else: 
        lives = 10
        print("You have 10 lives.")
    return lives

# While the player wants to continue playing
while try_again != False:
    greeting()
    number = random.randint(1,100)
    lives = select_level()
    # While lives are not over, 5 lives for hard, 10 for easy keep taking guesses
    while lives != 0:
        # Guess as input
        player_guess = int(input("Guess the number:\n"))
        # If player guessed the number right they win and the loop breaks
        if number == player_guess:
            print("Woohoo, you won!")
            break
        else: 
            # Otherwise, tell the player if they guessed higher or lower and reduce a life
            check_guess(number, player_guess)
            lives = lives - 1
            print(f"You have {lives} lives left.")
    # If the player is unable to guess they are given the option to play again
    if lives == 0:
        print("Sorry you lost!")
    again = input("Play again? Yes or no.")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        try_again = False
    else: 
        os.system('clear')