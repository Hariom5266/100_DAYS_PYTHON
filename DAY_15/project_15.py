# 🍵 , Hanji Kaise ho aap sabhi this is 15th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== COFFEE MACHINE ====================#
from main import MENU,resources,profit 

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made,False if ingritend are insufficient"""
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough=False
    return is_enough
    
def process_coins():
    """Return the total calculated from coins inserted"""
    print("please insert coins.")
    total=int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes?: "))*0.1
    total+=int(input("How many nickles?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total

def is_transaction_succesful(money_received,drink_cost):
    """Return True when payment is accepted, or False if money is insufficient"""
    if money_received>=drink_cost:
        change  = round(money_received-drink_cost,2)
        print(f"Here is ${change} in changes.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry there is not enough water.")
        return False
    
def make_coffe(drink_name,order_ingredients):
    "Deduct the required ingredients from the resources."
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕, Enjoy!")

is_on=True

while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    elif choice=="latte" or choice=="cappuccino" or choice=="espresso":
        drink=MENU[choice]        
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_succesful(payment,drink['cost']):
                make_coffe(choice,drink['ingredients'])
    else:
        print("Invalid choice,Enter valid choice.")



