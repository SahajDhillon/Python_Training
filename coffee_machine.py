import menu


def check_resources():
    coffee = menu.MENU[choice]
    if coffee['ingredients']['water'] <= menu.resources['water']:
        if coffee['ingredients']['milk'] <= menu.resources['milk']:
            if coffee['ingredients']['coffee'] <= menu.resources['coffee']:
                return True
            else:
                print("you are out of coffee!!")
                return False
        else:
            print("You are out of milk!!")
            return False
    else:
        print("You are out of water!!")
        return False


def transaction(coffee):
    pennies = float(input("Enter number of pennies: ")) * 0.01
    dimes = float(input("Enter number of dimes: ")) * 0.10
    quarters = float(input("Enter number of quarters: ")) * 0.25
    nickels = float(input("Enter number of nickels: ")) * 0.05
    total_money = pennies + dimes + quarters + nickels

    if menu.MENU[coffee]['cost'] >= total_money:
        print("Not Enough money. Returning money!")
    else:
        make_coffee(coffee)
        change = (total_money - menu.MENU[coffee]['cost']).__round__(2)
        print(f"Here's your change: {change}")


def make_coffee(choices):
    coffee = menu.MENU[choices]
    resources = menu.resources

    resources['milk'] -= coffee['ingredients']['milk']
    resources['water'] -= coffee['ingredients']['water']
    resources['coffee'] -= coffee['ingredients']['coffee']

    print(f"Your {choices} is ready at your table. Enjoy!")


if __name__ == '__main__':
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choice == 'report':
            print(menu.resources)
        elif choice == 'OFF':
            exit()
        elif check_resources():
            transaction(choice)

