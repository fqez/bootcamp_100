import random
from turtle import Turtle
from typing import List, Tuple

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEFT_EDGE = -300
RIGHT_EDGE = 300
RANDOM_RANGE = 600


class CarManager:
    """
    A class to manage the cars in the game.
    """

    def __init__(self):
        """
        Initializes a CarManager object.
        """
        self.cars: List[Turtle] = []

        for _ in range(10):
            self.add_car()
        self.increment = 0

    def add_car(self) -> None:
        """
        Adds a new car to the game.
        """
        car = Turtle()
        car.shape("square")
        car.seth(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))

        car.penup()
        car.goto(self.random_start_pos())
        self.cars.append(car)

    def move_cars(self) -> None:
        """
        Moves all the cars in the game.
        """
        for car in self.cars:

            car.forward(self.calculate_speed())
            if car.xcor() < LEFT_EDGE:
                self.move_to_new_position(car)

    def random_start_pos(self) -> Tuple[int, int]:
        """

        Generates a random starting position for a car.
        Returns:
            A tuple representing the x and y coordinates of the starting position.
        """
        return (RIGHT_EDGE + random.randint(0, RANDOM_RANGE), random.randint(-230, 250))

    def new_level(self) -> None:
        """
        Generates a new level by adding more cars to the game.
        """
        self.increment += 1

        num_cars = random.randint(1, int(2 * self.increment))
        for _ in range(num_cars):
            self.add_car()

    def check_collisions(self, player: Turtle) -> bool:
        """
        Checks if there is a collision between the player and any of the cars.
        Args:
            player: The player turtle object.
        Returns:
            True if there is a collision, False otherwise.
        """
        distances = map(player.distance, self.cars)
        return any(filter(lambda x: x < 35, distances))

    def calculate_speed(self) -> int:
        """

        Calculates the speed of the cars based on the current level.
        Returns:
            The speed of the cars.
        """
        return STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.increment)

    def move_to_new_position(self, car: Turtle) -> None:
        """
        Moves a car to a new random position.
        Args:
            car: The car to move.
        """
        car.goto(self.random_start_pos())
