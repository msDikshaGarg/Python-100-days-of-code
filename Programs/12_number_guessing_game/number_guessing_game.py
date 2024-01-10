import random
import os
from artwork import art

def greeting():
    print(art)
    print("You are now playing the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

lives = 0
try_again = True

def check_guess(num, guess):
    if num - guess < 0 and abs(num - guess) >= 10: 
        print("Too high!")
    elif num - guess < 0 and abs(num - guess) < 10: 
        print("Close but high!")
    elif num - guess >= 10:
        print("Too low!")
    else: 
        print("Close but low!")

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

while try_again != False:
    greeting()
    number = random.randint(1,100)
    lives = select_level()

    while lives != 0:
        player_guess = int(input("Guess the number:\n"))
        if number == player_guess:
            print("Woohoo, you won!")
            break
        else: 
            check_guess(number, player_guess)
            lives = lives - 1
            print(f"You have {lives} lives left.")

    if lives == 0:
        print("Sorry you lost!")
    again = input("Play again? Yes or no.")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        try_again = False
    else: 
        os.system('clear')