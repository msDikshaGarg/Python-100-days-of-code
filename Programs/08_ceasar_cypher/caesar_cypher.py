# Importing libraries and relevant files
import string
from artwork import art

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

# While user doesn't want to end the program 
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
# Prints a goodbye message on exit
print("Thank you! Goodbye.")
        