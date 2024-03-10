import random
from turtle import Turtle

FOOD_SIZE = 0.5
FOOD_SPEED = "fastest"


class Food(Turtle):
    """A class representing the food in the game."""

    def __init__(self, width, height):
        """Initialize the food."""
        super().__init__()

        self.width = width
        self.height = height

        self._init_turtle()

    def _init_turtle(self):
        """Initialize the turtle."""
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.speed(FOOD_SPEED)
        self.goto(self.random_position)

    @property
    def random_position(self):
        """Generate a random position within the screen boundaries."""
        posx = random.randint(-self.width // 2 + 40, self.width // 2 - 40)
        posy = random.randint(-self.height // 2 + 40, self.height // 2 - 40)
        return posx, posy

    def create_new(self):
        """Move the food to a new random position."""
        self.goto(self.random_position)
