# Importing the relevant libraries and files
import random
import string
from artwork import art

# Generating a list of lowercase and uppercase alphabets using the string module
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
alphabets = lowercase + uppercase
# Number and symbol lists
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

# Greeting
print(art)
print("Welcome to Spies and Sons Inc.!\nThis is where we will generate your super secret password.")

# Taking the number of each element user wants in their password
num_alpha =int(input("How many alphabets do you want in the password?\n"))
num_nums = int(input("How many numbers?\n"))
num_symbol = int(input("How many symbols?\n"))

# Declairing choice and password variables
password = ''
choice = ''

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
print(f"Your new password is: {password}")
    