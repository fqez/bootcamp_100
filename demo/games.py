import time
import random
from typing import Dict, List

import os

from faker import Faker

from asts import ROCK, PAPER, SCISSORS, stages, hl_data, hl_logo, hl_vs


def choose_adventure() -> None:
    """
    Play the Choose Your Own Adventure game.
    """
    steps: Dict[str, Dict[str, str]] = {
        "start": {"message": "You are in a forest. Do you want to go 'left' or 'right'? ", "left": "lake", "right": "game_over"},
        "lake": {"message": "You find a lake. Do you want to go 'swim' or 'wait'? ", "swim": "cave", "wait": "game_over"},
        "cave": {"message": "You find a cave. Do you want to go 'enter' or 'leave'? ", "enter": "doors", "leave": "game_over"},
        "doors": {"message": "You find 3 doors. Do you want to go 'red', 'blue' or 'yellow'? ", "red": "game_over", "blue": "game_over", "yellow": "win"},
        "game_over": {"message": "Game Over"},
        "win": {"message": "You win!"}
    }

    current_step: str = "start"

    input("Welcome to the Choose Your Own Adventure game. Press Enter to start.")

    while True:
        step: Dict[str, str] = steps[current_step]
        choice: str = input(step["message"])
        if choice in step:
            current_step = step[choice]
        else:
            print("Invalid choice. Please try again.")
        if current_step in ["game_over", "win"]:
            print(steps[current_step]["message"])
            break


def tressure_map() -> None:
    """
    Create a treasure map and hide the treasure.
    """
    line1: List[str] = ["⬜️", "⬜️", "⬜️"]
    line2: List[str] = ["⬜️", "⬜️", "⬜️"]
    line3: List[str] = ["⬜️", "⬜️", "⬜️"]

    choices: Dict[str, int] = {"A": 0, "B": 1, "C": 2}
    MAP: List[List[str]] = [line1, line2, line3]

    print("Hiding your treasure! X marks the spot!")

    position: str = input("Where do you want to put the treasure? ")

    MAP[int(position[1])-1][choices[position[0]]] = "❌"

    print(f"{line1}\n{line2}\n{line3}")


def rock_paper_scissors() -> None:
    """
    Play Rock, Paper, Scissors.
    """

    options = [ROCK, PAPER, SCISSORS]

    print("Welcome to Rock, Paper, Scissors!")
    user_choice = int(
        input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
    cpu_choice = random.randint(1, 3)
    result = (user_choice - cpu_choice) % 3

    print(f"You chose:\n{options[user_choice-1]}\n\n VS.\n\n")
    print(f"Computer chose:\n{options[cpu_choice-1]}")

    if result == 0:
        print("It's a draw!")
    elif result == 1:
        print("You win!")
    else:
        print("You lose!")


def hangman() -> None:
    """
    Play Hangman.
    """

    lives = 6
    fake = Faker()
    random_word = list(fake.word())

    display = list("_"*len(random_word))

    while lives > 0:
        guess = input("Guess a letter: ").lower()
        if guess in random_word:
            indices = [i for i, letter in enumerate(
                random_word) if letter == guess]
            for index in indices:
                display[index] = guess
        else:
            lives -= 1
            print(f"\nYou have {lives} lives left.")
            print(stages[lives])

        print(" ".join(display))

        if "".join(display) == "".join(random_word):
            break

    if lives == 0:
        print("\n\nYou lose! the word was: ", "".join(random_word))
    else:
        print("\n\nYou win!")


def blackjack():
    """
    Play a game of blackjack.
    """

    def check_win(player_score: int, cpu_score: int) -> None:
        """
        Check the winner of the blackjack game.

        Args:
            player_cards (List[int]): The cards of the player.
            cpu_cards (List[int]): The cards of the CPU.
            player_score (int): The score of the player.
            cpu_score (int): The score of the CPU.
        """
        if player_score > 21 and cpu_score > 21:
            print("It's a tie!")
        elif player_score == 21 or (player_score > cpu_score and player_score < 21) or cpu_score > 21:
            print("You win!")
        elif cpu_score == 21 or (cpu_score > player_score and cpu_score < 21) or player_score > 21:
            print("CPU wins!")
        else:
            print("It's a tie!")

    def draw_card(deck: List[int]) -> int:
        """
        Draw a card from the deck.

        Args:
            deck (List[int]): The deck of cards.

        Returns:
            int: The drawn card.
        """
        return deck.pop(random.randrange(len(deck)))

    def print_status(player_cards: List[int], cpu_cards: List[int], player_score: int, cpu_score: int) -> None:
        """
        Print the status of the game.

        Args:
            player_cards (List[int]): The cards of the player.
            cpu_cards (List[int]): The cards of the CPU.
            player_score (int): The score of the player.
            cpu_score (int): The score of the CPU.
        """
        print("\n" + "=" * 30)
        print("Your cards:")
        print(' '.join([" _____ " for card in player_cards]))
        print(' '.join([f"|{card:^5}|" for card in player_cards]))
        print(' '.join(["|     |" for card in player_cards]))
        print(' '.join(["|_____|" for card in player_cards]))
        print(f"Your score: {player_score}")
        print("-" * 30)
        print("CPU cards:")
        print(' '.join([" _____ " for card in cpu_cards]))
        print(' '.join([f"|{card:^5}|" for card in cpu_cards]))
        print(' '.join(["|     |" for card in cpu_cards]))
        print(' '.join(["|_____|" for card in cpu_cards]))
        print(f"CPU score: {cpu_score}")
        print("=" * 30 + "\n")

    cards: List[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    player_cards: List[int] = []
    player_score: int = 0
    cpu_cards: List[int] = []
    cpu_score: int = 0

    random.shuffle(cards)

    while (input("Do you want a card? (y/n): ")) == 'y':

        if cards:
            player_cards.append(draw_card(cards))
            player_score = sum(player_cards)
        else:
            print("No more cards!")
            break

        if sum(cpu_cards) < 17:
            cpu_cards.append(draw_card(cards))
            cpu_score = sum(cpu_cards)

        print_status(player_cards, cpu_cards, player_score, cpu_score)

        if player_score >= 21 or cpu_score >= 21:
            break

    if sum(cpu_cards) < 17:
        cpu_cards.append(draw_card(cards))
        cpu_score = sum(cpu_cards)
        print_status(player_cards, cpu_cards, player_score, cpu_score)

    check_win(player_score, cpu_score)


def guess_number() -> None:
    """
    Play a game of guessing a number.
    """
    lives: int = 5
    number: int = random.randint(1, 100)

    print("Welcome to the Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100.")

    while lives > 0:
        guess: int = int(input("\nGuess a number: "))
        print("Let's see if you're right...")
        time.sleep(2)

        if guess == number:
            print("🎉 Congratulations! You guessed the number! 🎉")
            break
        elif guess < number:
            print(f"😅 Oops! Your guess is too low. Don't worry, you can try again. You have \
                  {lives} lives left.")
        else:
            print(f"😅 Oops! Your guess is too high. Don't worry, you can try again. You have \
                  {lives} lives left.")
        lives -= 1

    if lives == 0:
        print(f"😢 Sorry, you didn't guess the number. The correct number was: \
              {number}. Better luck next time!")


def higher_lower():

    def print_challenge(pick1, pick2):
        print(f"Compare A: {pick1['name']}, a {
              pick1['description']}, from {pick1['country']}")
        print(hl_vs)
        print(f"Against B: {pick2['name']}, a {
              pick2['description']}, from {pick2['country']}")
        print("\n")

    def print_final_screen():
        os.system('cls')
        print(hl_logo)
        print(f"Your final score is: {score}")

    def check_correct(guess, pick1, pick2):
        if pick1['follower_count'] > pick2['follower_count']:
            return guess == 'a'
        else:
            return guess == 'b'

    def reset_screen():
        os.system('cls')
        print(hl_logo)
        print(f"Your current score is: {score}")

    os.system('cls')
    print(hl_logo)
    alive = True
    score = 0

    while alive:

        n1 = random.randint(0, len(hl_data)-1)
        while n1 == (n2 := random.randint(0, len(hl_data)-1)):
            n2 = random.randint(0, len(hl_data)-1)

        pick1, pick2 = hl_data[n1], hl_data[n2]

        print_challenge(pick1, pick2)
        print("DEGUB: ", pick1['follower_count'], pick2['follower_count'])

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if not check_correct(guess, pick1, pick2):
            print("You're wrong! Game over!")
            print_final_screen()
            alive = False
        else:
            score += 1
            reset_screen()


if __name__ == '__main__':

    higher_lower()
