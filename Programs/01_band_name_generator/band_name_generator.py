# Importing os to clear screen and art from artwork.py
import os
from artwork import art

# Play again flag set to True
play_again = True

while play_again != False:
    print(art)

    # Asking city name 
    print("Let's generate a cool band name for you.\n")
    city = input("Name a random place.\n")

    # Asking pet name 
    animal = input("Name a random animal in plural.\n")

    # Printing band name 
    print("Congratulations, your band name is ... " + city + " " + animal + "!")

    # Play again loop: if the player wants to exit the play_again flag sets to false and we exit the main loop
    again = input("Type 'Yes' to play again or 'No' to exit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        play_again = False
    else: 
        os.system('clear')
