from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_running = True

while machine_is_running:
    menulist = menu.get_items()
    user_input = input(f"What would you like? ({menulist}): ").lower()
    if user_input == 'off':
        machine_is_running = False
    
    elif user_input == 'report':
        coffee_machine.report()
        money_machine.report()
    
    else:
        order = menu.find_drink(user_input)

        if order is None:
            continue
        
        if not coffee_machine.is_resource_sufficient(order):
            continue
        
        if money_machine.make_payment(order.cost):
            coffee_machine.make_coffee(order)
