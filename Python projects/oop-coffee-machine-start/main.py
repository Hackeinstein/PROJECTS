from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

#set objects
machine = CoffeeMaker()
cashier=MoneyMachine()
menulist=Menu()

# get users choice 
state=True
def run_store():
    state=True
    choice = input(f"What would you like {menulist.get_items()}: ")
    #check value to see if it contains special keywords
    if choice == "off":
        state=False
    elif choice == "report":
        machine.report()
    else:
        #get the item from list and check for quantity
        drink=menulist.find_drink(choice)
        #check the items required to make and compare
        if machine.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                #carry on and make drink
                machine.make_coffee(drink)
        else:
            print("Not enough ingredients")
    return state
#keep looping
while state:
    state=run_store()

