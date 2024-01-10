# Importing needed libraries and files
import os
from artwork import art

# Play again flag set to True
play_again = True

while play_again != False:
    # Printing greeting
    print(art)
    print("Let's generate a cool band name for you.\n")

    # Asking for a city name 
    city = input("Name a random place.\n")

    # Asking for an animal name 
    animal = input("Name a random animal in plural.\n")

    # Printing band name 
    print("Congratulations, your band name is ... " + city + " " + animal + "!")

    # Play again loop: if the player wants to exit 
    # the play_again flag sets to false and we exit the main loop
    again = input("Type 'Yes' if you want to generate a new name or 'No' to exit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        play_again = False
    else: 
        os.system('clear')
