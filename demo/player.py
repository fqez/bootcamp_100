from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UPWARDS = 90


class Player(Turtle):
    def __init__(self):
        """Initialize the Player object."""

        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

        self.seth(UPWARDS)

    def move(self):
        """Move the player forward by the defined distance."""
        self.forward(MOVE_DISTANCE)

    def check_won(self) -> bool:
        """Check if the player has reached the finish line.

        Returns:
            bool: True if the player has reached the finish line, False otherwise.
        """
        if self.has_reached_finish_line():
            self.reset_position()

            return True
        else:
            return False

    def reset_position(self):
        """Reset the player's position to the starting position."""
        self.goto(STARTING_POSITION)

    def has_reached_finish_line(self) -> bool:
        """Check if the player has reached or passed the finish line.

        Returns:
            bool: True if the player has reached or passed the finish line, False otherwise.
        """
        return self.ycor() >= FINISH_LINE_Y
