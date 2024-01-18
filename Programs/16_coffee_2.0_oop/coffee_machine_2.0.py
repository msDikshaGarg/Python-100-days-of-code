from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#menu_options = MenuItem()
menu_full = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

machine_state = True
while machine_state:
    options = menu_full.get_items()
    order = input(f"What would you like to order today? ({options})\n")
    while order not in ['off', 'report', 'espresso', 'latte', 'cappuccino']:
        order = input("Sorry we don't serve that. Try again.\n")
    if order == 'off':
        machine_state = False
    elif order == 'report':
        machine.report()
        money_machine.report()
    else:
        drink = menu_full.find_drink(order)
        if machine.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost) == True:
                machine.make_coffee(drink)
