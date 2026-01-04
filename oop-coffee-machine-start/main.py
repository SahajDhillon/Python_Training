from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True

while is_on:
    choice = input(f"What would yoy like to have ? {menu.get_items()}").lower()
    if choice == "report":
        money_machine.report()
        coffee_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)


