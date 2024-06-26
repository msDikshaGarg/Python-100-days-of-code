# Importing libraries and artwork files
import random
from artwork import rock_art, paper_art, scissor_art

# List for possible choices and their respective arts
image = [rock_art, paper_art, scissor_art]
choice = ['rock', 'paper', 'scissor']

# Option to play again
play_again = True

# Counters for total number of player wins and computer wins
player_wins = 0
computer_wins = 0

# Making the try again function to add the option to play again
def try_again():
    again = input(f"Want to go again? Yes or No.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        return False
    else: 
        return True

while play_again == True:
# Taking player choice 
    player = input("Rock, Paper, Scissor. Choose!\n").lower()
    while player not in choice:
        player = input("Please enter a valid input.\n").lower()
    # Printing player choice art
    player_num = choice.index(player)
    print(image[player_num])
    # Selecting a random computer choice and printing the choice with art
    computer = random.randint(0,2)
    print(f"The computer chooses {choice[computer]}")
    print(image[computer])

    # Checking the result based on user and computer choices and printing the outcome
    if player_num == computer:
        print("It's a tie.")
        print(f"You have won {player_wins} times and the computer has won {computer_wins} times.")
    elif (player_num == 2 and computer == 0) or (player_num < computer):
        print("Sorry you lost.")
        computer_wins += 1
        print(f"You have won {player_wins} times and the computer has won {computer_wins} times.")
    else: 
        print("Woohoo! You are a champion.")
        player_wins += 1
        print(f"You have won {player_wins} times and the computer has won {computer_wins} times.")
    play_again = try_again()
