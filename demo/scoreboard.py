from turtle import Turtle

FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    """
    A class representing a scoreboard for a game.
    """

    def __init__(self):
        """

        Initializes a new instance of the Scoreboard class.
        """
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()

        self.goto(-280, 250)
        self._level = 1
        self.update_level()

    def update_level(self):
        """
        Updates the level displayed on the scoreboard.

        """
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increment_level(self):
        """
        Increments the level by 1 and updates the scoreboard.

        """
        self.level += 1
        self.update_level()

    def game_over(self):
        """
        Displays the "Game Over!" message on the scoreboard.

        """
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    @property
    def level(self) -> int:
        """

        Gets the current level.

        Returns:
            The current level.
        """
        return self._level

    @level.setter
    def level(self, value: int):
        """
        Sets the current level.

        Args:
            value: The new level value.
        """
        self._level = value
