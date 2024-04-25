# Importing the relevant libraries and files
import random
import string

def password_generator():
    # Generating a list of lowercase and uppercase alphabets using the string module
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    alphabets = lowercase + uppercase
    # Number and symbol lists
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    # Taking the number of each element user wants in their password
    num_alpha = random.randint(5,8)
    num_nums = random.randint(2,4)
    num_symbol = random.randint(1,3)

    # Declairing choice and password variables
    password = ''

    # Adding the specified number of random alphabets, number and symbols to the password
    for n in range(0,num_alpha):
        password += random.choice(alphabets)
    for n in range(0,num_nums):
        password += random.choice(numbers)
    for n in range(0,num_symbol):
        password += random.choice(symbols)

    # Shuffling the order of elements in password
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Printing the final password
    return password
        