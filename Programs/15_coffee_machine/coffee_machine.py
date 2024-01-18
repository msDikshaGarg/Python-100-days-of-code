# Import from file
from presets import MENU, resources, art_coffee_cup, art_coffee_machine

# Initializing variables
manual_stop = False
money = 0
curr_resources = resources.copy()

# Function to print report of ingredients
def print_report():
    print(f"Water : {curr_resources['water']}ml")
    print(f"Milk : {curr_resources['milk']}ml")
    print(f"Coffee : {curr_resources['coffee']}g")
    print(f"Money : ${money}")

# Function to ask for coins and calculating the total money put into the machine
def take_money():
    total = 0
    print("Please insert coins for your coffee.")
    quarters = int(input("No of quarters: "))
    dimes = int(input("No of dimes: "))
    nickles = int(input("No of nickles: "))
    pennies = int(input("No of pennies: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

# Function to check if all ingredients are available, if an ingredient is missing the machine prints out a message with the missing ingredient name
def availability(coffee_type):
    details =  MENU[coffee_type]
    needs = details["ingredients"]
    for key in needs:
        if needs[key] > curr_resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
        else: 
            return details["cost"]

# Function to check if the money put into the machine is enough for the order  
def check_money(cost, total):
    if total - cost < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return [total - cost]

# Function to update ingredients once a coffee is served
def update_resources(coffee_type):
    details =  MENU[coffee_type]
    needs = details["ingredients"]
    for key in needs:
        curr_resources[key] = curr_resources[key] - needs[key]

# Function to refill the coffee machine
def refill_resources():
    for key in curr_resources:
        curr_resources[key] = resources[key]

# Greeting
print(art_coffee_machine)
print("LET'S GET BREWING!\n\n")

# If the barista hasn't stopped the program
while manual_stop == False:
    # Take customer's coffee order
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # If the customer gave an invalid command, ask for a valid input
    while command not in ['off', 'report', 'refill', 'espresso', 'latte', 'cappuccino']:
        command = input("Sorry we don't serve that. Our menu options are (espresso/latte/cappuccino): ")
    # if the barista selects stop, the machine stops operating
    if command == 'off':
        manual_stop = True
        break
    # Else if barista types report, then the report function runs to print a report of ingredients
    elif command == 'report':
        print_report()
    # Else if barista types refill, the machine refills the ingredients
    elif command == 'refill':
        curr_resources = resources.copy()
        print("The machine has been refilled.")
    else:
        # For the order, check if all ingredients are available 
        coffee_cost = availability(command)
        if coffee_cost != False:
            # If ingredients are available, take money
            money_inserted = take_money()
            change = check_money(coffee_cost, money_inserted)
            if change != False:
                # If money is enough, update resources, add money to earnings and check for change
                update_resources(command)
                money += coffee_cost
                # If change is 0 then serve the coffee and prompt again
                if change[0] == 0:
                    print(f"Here is your {command}. Enjoy!")
                    print(art_coffee_cup)
                else: 
                    # Else serve the coffee and provide change
                    print(f"Here is your {command}. Enjoy!")
                    print(art_coffee_cup)
                    print(f"Here is ${round(change[0],2)} dollars in change.")

