# Random band name generator
import os

# Greeting
art = """
 ____                  _                              
| __ )  __ _ _ __   __| |  _ __   __ _ _ __ ___   ___ 
|  _ \ / _` | '_ \ / _` | | '_ \ / _` | '_ ` _ \ / _ \\
| |_) | (_| | | | | (_| | | | | | (_| | | | | | |  __/
|____/ \__,_|_| |_|\__,_| |_| |_|\__,_|_| |_| |_|\___|
  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __        
 / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|       
| (_| |  __/ | | |  __/ | | (_| | || (_) | |          
 \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|          
 |___/                                                
\n\n
"""

play_again = True

while play_again != False:
    print(art)
    # Asking city name 
    print("Let's generate a cool band name for you.\n")
    city = input("Name a random place.\n")

    # Asking pet name 
    animal = input("Name a random animal.\n")

    # Printing band name 
    print("Congratulations, your band name is ... " + city + " " + animal + "!")

    again = input("Type 'Yes' to play again or 'No' to exit.\n")
    while again not in ['yes', 'no']:
        again = input("Please enter a valid input.\n").lower()
    if again == 'no':
        play_again = False
    else: 
        os.system('clear')
