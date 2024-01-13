from presets import MENU, resources, art_coffee_cup, art_coffee_machine
import copy

manual_stop = False
money = 0
curr_resources = resources.copy()

def print_report():
    print(f"Water : {curr_resources['water']}ml")
    print(f"Milk : {curr_resources['milk']}ml")
    print(f"Coffee : {curr_resources['coffee']}g")
    print(f"Money : ${money}")

def take_money():
    total = 0
    print("Please insert coins for your coffee.")
    quarters = int(input("No of quarters: "))
    dimes = int(input("No of dimes: "))
    nickles = int(input("No of nickles: "))
    pennies = int(input("No of pennies: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

def availability(coffee_type):
    details =  MENU[coffee_type]
    needs = details["ingredients"]
    for key in needs:
        if needs[key] > curr_resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
        else: 
            return details["cost"]
        
def check_money(cost, total):
    if total - cost < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return [total - cost]
    
def update_resources(coffee_type):
    details =  MENU[coffee_type]
    needs = details["ingredients"]
    for key in needs:
        curr_resources[key] = curr_resources[key] - needs[key]
        
def refill_resources():
    for key in curr_resources:
        curr_resources[key] = resources[key]

print(art_coffee_machine)
print("LET'S GET BREWING!\n\n")

while manual_stop == False:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while command not in ['off', 'report', 'refill', 'espresso', 'latte', 'cappuccino']:
        command = input("Sorry we don't serve that. Our menu options are (espresso/latte/cappuccino): ")
    if command == 'off':
        manual_stop = True
        break
    elif command == 'report':
        print_report()
    elif command == 'refill':
        curr_resources = resources.copy()
        print("The machine has been refilled.")
    else:
        coffee_cost = availability(command)
        if coffee_cost != False:
            money_inserted = take_money()
            change = check_money(coffee_cost, money_inserted)
            if change != False:
                update_resources(command)
                money += coffee_cost
                if change[0] == 0:
                    print(f"Here is your {command}. Enjoy!")
                    print(art_coffee_cup)
                else: 
                    print(f"Here is your {command}. Enjoy!")
                    print(art_coffee_cup)
                    print(f"Here is ${round(change[0],2)} dollars in change.")

