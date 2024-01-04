import os

# Greeting
logo = """
 _____________________
|  _________________  |     _         _   _                  _   
| | Python calc 2.0 | |    | |    ___| |_( )___    __ _  ___| |_   
| |_________________| |    | |   / _ \ __|// __|  / _` |/ _ \ __|  
|  ___ ___ ___   ___  |    | |__|  __/ |_  \__ \ | (_| |  __/ |_
| | 7 | 8 | 9 | | + | |    |_____\___|\__| |___/ _\__, |\___|\__| 
| |___|___|___| |___| |    |  \/  | __ _| |_| |___(_)_ __   __ _ 
| | 4 | 5 | 6 | | - | |    | |\/| |/ _` | __| '_ \| | '_ \ / _` |
| |___|___|___| |___| |    | |  | | (_| | |_| | | | | | | | (_| |
| | 1 | 2 | 3 | | x | |    |_|  |_|\__,_|\__|_| |_|_|_| |_|\__, | 
| |___|___|___| |___| |                                    |___/ 
| | . | 0 | = | | / | | 
| |___|___|___| |___| | 
|_____________________|  \n\n

"""
# Addition 
def add(a,b):
    return a + b

# Subtraction
def subtract(a,b):
    return a - b

# Multiplication
def multiply(a,b):
    return a * b

# Division
def divide(a,b):
    return a / b

# Dictionary of operation functions
operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

# Main function
def calculator():
    # Printing logo
    print(logo)
    # Variable input (first)
    n1 = int(input("What's the first number?\n"))

    # While loop to check if the user wants to continue calculating if yes then steps repeat with n1 = value
    while True:
        # Operation and second number inputs
        op = input("What operation would you like to perform?\n +, -, * or /\n")
        n2 = int(input("What's the next number?\n"))
        # Calculation
        calculation = operations[op]
        value = round(calculation(n1,n2),2)
        print(f"{n1} {op} {n2} = {value}")
        # User input to continue or not
        go_on = input("Would you like to go on or start fresh?\n Type Y to continue or N to start again.\n").lower()
        while go_on not in ['y', 'n']:
            go_on = input("Please enter a valid input.\n").lower()
        # If user says continue then n1 becomes value
        if go_on == 'y':
            n1 = value
        # Else it clears the screen and starts the function again
        else: 
            os.system('clear')
            calculator()

calculator()
