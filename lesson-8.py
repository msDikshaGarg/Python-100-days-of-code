## Fix if number larger than 26 -> mod

import string
# Greeting
art = """
 ____        _                             _   ____                  
/ ___| _ __ (_) ___  ___    __ _ _ __   __| | / ___|  ___  _ __  ___ 
\___ \| '_ \| |/ _ \/ __|  / _` | '_ \ / _` | \___ \ / _ \| '_ \/ __|
 ___) | |_) | |  __/\__ \ | (_| | | | | (_| |  ___) | (_) | | | \__ \\
|____/| .__/|_|\___||___/  \__,_|_| |_|\__,_| |____/ \___/|_| |_|___/
|_ _|_|_|   ___                                                      
 | || '_ \ / __|                                                     
 | || | | | (__ _                                                    
|___|_| |_|\___(_)      \n\n     
"""
# List of alphabets to create cypher
alphabets = list(string.ascii_lowercase)*2

# Cypher function definition
def cypher(funct, message, shift):
    # If decoding then shift number gets subtracted
    shift = shift % 26
    if funct == 'decode':
        shift = shift * -1
    new_message = ''
    # Looping through the message and adding / subtracting the shift number to generate new encoded / decoded message 
    for i in list(message):
        if i in alphabets:
            curr_index = alphabets.index(i)
            new_message += alphabets[curr_index + shift]
        else: 
            # If a symbol or spaces exist which are not in alphabets then it just adds them as it is 
            new_message += i
    print(f"Your {funct}d message is : '{new_message}'")

# Ending program flag
end = False 

# While user doesn't want to run program 
while end == False:
    print(art)
    print("Welcome to Spies and Sons Inc.!\nWe are back again with our special spy encryption and decryption machine.")
    # Takes user inputs
    funct = input("Do you want to encode or decode?\n").lower()
    message = input("Type a message:\n").lower()
    shift = int(input("What's the secret shift number?\n"))
    
    # Calls the function for output
    cypher(funct, message, shift)
    
    # Checks if user wants to end, chenges the flag if user selects yes
    ending = input("\nIs this the message you want to continue with? Type 'Y' for yes, 'N' for no.\n").lower()
    while ending not in ['y', 'n']:
        ending = input("Please enter a valid input.\n").lower()
    if ending == 'y':
        end = True
print("Thank you! Goodbye.")
        