import random
from typing import List


def count_characters(name: str) -> int:
    """
    Count the number of characters in a string.

    Args:
        name (str): The string to count characters from.

    Returns:
        int: The number of characters in the string.
    """
    return len(name)


def is_leap(year: int) -> bool:
    """
    Check if a year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def generate_random_numbers(n: int) -> List[int]:
    """
    Generate a list of n random numbers.

    Args:
        n (int): The number of random numbers to generate.

    Returns:
        List[int]: A list of n random numbers.
    """
    return [random.randint(0, 100) for _ in range(n)]


def buzz() -> None:
    """
    Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def password_generator() -> str:
    """
    Generates a random password based on user input.

    The function prompts the user to enter the desired length of the password.
    It then generates a password containing a combination of letters, symbols, and numbers.
    The number of letters, symbols, and numbers in the password is determined randomly.

    Returns:
        str: The generated password.
    """
    letters: List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols: List[str] = ["!", "@", "#", "$", "%", "^", "&", "*",
                          "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]
    numbers: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    length: int = int(input("How long would you like your password to be? "))

    n_numbers: int = random.randint(4, length-2)
    n_symbols: int = random.randint(1, length-n_numbers-1)
    n_letters: int = length - n_numbers - n_symbols

    password: List[str] = [random.choice(letters) for _ in range(n_letters)] + [random.choice(symbols)
                                                                                for _ in range(n_symbols)] + [random.choice(numbers) for _ in range(n_numbers)]

    random.shuffle(password)
    password = ''.join(password)

    return password


def check_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def caesar_cypher(text: str, shift: int) -> str:
    """
    Encrypt or decrypt a message using the Caesar cypher.

    Args:
        text (str): The message to be encrypted or decrypted.
        shift (int): The number of positions to shift the letters.

    Returns:
        str: The encrypted or decrypted message.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_amount +
                                  shift) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == '__main__':

    pass
