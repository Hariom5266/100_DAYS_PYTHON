# 🍵 , Hanji Kaise ho aap sabhi this is 16th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== Coffee Machine -- OOP Version ====================== #

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# snake case
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_on=True

# coffee_maker.report()
# money_machine.report()

while is_on:
    options=menu.get_items()
    choice=input(f"What would you like? ({options}): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)        
        # print(drink)
        # print(coffee_maker.is_resource_sufficient(drink))
        if coffee_maker.is_resource_sufficient(drink):
            # print(money_machine.make_payment(drink.cost))
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


