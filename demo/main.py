from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu: Menu = Menu()
coffee_maker: CoffeeMaker = CoffeeMaker()
money_machine: MoneyMachine = MoneyMachine()

while 1:

    choice: str = input(f"Please, choose an option from {menu.get_items()}")

    match choice:
        case 'off':
            break
        case 'report':
            coffee_maker.report()
            money_machine.report()

        case _:
            drink: MenuItem = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print("Sorry, not enough resources")
                break
