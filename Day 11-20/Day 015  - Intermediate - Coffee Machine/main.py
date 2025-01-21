MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_order():
    """returns the order of the of the customer as a string"""
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def display_report():
    """display resources report"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${profit}")

def is_enough_resources(coffee):
    """checks if there are enough resources in the coffee machine to make the order"""
    for key in coffee:
        if coffee[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def get_coins():
    """returns the sum total of the coins based on the coin type"""
    print("Please insert coins.")
    total = float(input("how many quarters? ")) * 0.25
    total += float(input("how many dimes? ")) * 0.10
    total += float(input("how many nickels? ")) * 0.05
    total += float(input("how many pennies? ")) * 0.01
    return total

def successful_transaction(user_money, order_cost):
    """returns the order cost and calculate the change"""
    global profit
    profit += order_cost
    change = user_money - order_cost
    print(f"Here is ${round(change,2)} in change.")
    return order_cost

def make_coffee(coffee):
    """makes the coffee ordered and takes ingredients from the resources"""
    order_ingredients = MENU[coffee]["ingredients"]
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f"Here is your {coffee} ☕️. Enjoy!")

def coffee_machine():
    """
    Simulates the operation of a coffee machine.
    The function runs an infinite loop where it continuously takes orders from the user until the machine is turned off.
    It processes the following commands:
    - 'off': Turns off the coffee machine.
    - 'report': Displays the current resource report.
    - Any other valid coffee order: Checks if there are enough resources and if the user has inserted enough money to make the coffee.
    The function performs the following steps for each coffee order:
    1. Checks if there are enough resources to make the coffee.
    2. Prompts the user to insert coins and checks if the inserted money is sufficient.
    3. If the money is sufficient, it updates the profit and makes the coffee.
    4. If the money is not sufficient, it refunds the money to the user.
    Global Variables:
    - profit (float): The total profit made by the coffee machine.
    Returns:
    None
    """
    machine_is_running = True
    while machine_is_running:
        order = get_order()
        if order == 'off':
            machine_is_running = False
        elif order == 'report':
            display_report()
        else:
            order_cost = MENU[order]["cost"]
            order_ingredients = MENU[order]["ingredients"]
            
            if not is_enough_resources(order_ingredients):
                continue

            user_money = get_coins() 
            is_enough_money = user_money >= order_cost
 
            if not is_enough_money:
                print("Sorry that's not enough money. Money is refunded.")
                continue

            successful_transaction(user_money, order_cost)
            make_coffee(order)

# main
coffee_machine()
