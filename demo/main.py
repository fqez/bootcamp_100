import os
from typing import Dict, Any

MENU: Dict[str, Dict[str, Any]] = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    }
}

resources: Dict[str, Dict[str, Any]] = {
    "water": {"amount": 300, "unit": "ml", "default": 300},
    "milk": {"amount": 200, "unit": "ml", "default": 200},
    "coffee": {"amount": 100, "unit": "g", "default": 100},
    "money": {"amount": 0, "unit": "€"}
}


def print_report() -> None:
    """Prints the current status of resources."""
    for key, value in resources.items():
        print(f"{key.capitalize()}: {value['amount']}{value['unit']}")


def refill() -> None:
    """Refills the resources to their default amounts."""
    for value in resources.values():
        if "default" in value:
            value["amount"] = value["default"]


def check_enough_resources(choice: str) -> bool:
    """Checks if there are enough resources to make the selected drink.

    Args:
        choice: The selected drink.

    Returns:
        True if there are enough resources, False otherwise.
    """
    if (resources['water']['amount'] - MENU[choice]['ingredients']['water'] <= 0):
        print("There's not enough water")
        return False
    elif (resources['coffee']['amount'] - MENU[choice]['ingredients']['coffee'] <= 0):
        print("There's not enough coffee")
        return False
    elif (resources['milk']['amount'] - MENU[choice]['ingredients']['milk'] <= 0):
        print("There's not enough milk")
        return False

    return True


def update_resources(choice: str, qty: float) -> None:
    """Updates the resources after a drink is made.

    Args:
        choice: The selected drink.
        qty: The amount of money inserted.

    Returns:
        None
    """
    resources['water']['amount'] -= MENU[choice]['ingredients']['water']
    resources['coffee']['amount'] -= MENU[choice]['ingredients']['coffee']
    resources['milk']['amount'] -= MENU[choice]['ingredients']['milk']
    resources['money']['amount'] += MENU[choice]['cost']


def process_selection(choice: str) -> bool:
    """Processes the user's drink selection.

    Args:
        choice: The selected drink.

    Returns:
        True if the drink is successfully made, False otherwise.
    """
    if not check_enough_resources(choice):
        return False

    print(f"This item costs: {MENU[choice]['cost']}€")

    if ((qty := float(input("Please insert money: "))) >= (cost := MENU[choice]['cost'])):
        print(f"Your change is {qty - cost}")
        update_resources(choice, cost-qty)
        return True
    else:
        print(f"Not enough cash. Money refunded")
        return False


def start() -> None:
    """Starts the coffee machine program."""
    while 1:
        match choice := input("What would you like? (Espresso/Latte/Cappuccino/off): ").lower():
            case 'espresso' | 'latte' | 'cappuccino':
                if process_selection(choice):
                    print(f"Here's your {choice.capitalize()} 🍵. Enjoy!")
                    print("\n\n/--------------------------------------------\\\n")
                else:
                    break

            case 'report':
                print('report')
                print_report()

            case 'refill':
                print('refill')
                refill()

            case 'off':
                break

            case _:
                print("Invalid option. Please, try again!")


if __name__ == "__main__":
    start()
