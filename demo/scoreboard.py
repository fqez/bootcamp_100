from turtle import Turtle

from constants import ALIGNMENT, FONT, SCORE_L_POS, SCORE_R_POS


class Scoreboard(Turtle):
    """A class representing the game scoreboard."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()

        self.l_score = 0
        self.r_score = 0

        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(SCORE_L_POS)
        self._writea(f"{self.l_score}")
        self.goto(SCORE_R_POS)
        self._writea(f"{self.r_score}")

    def point(self, player):
        self.goto(0, 0)
        if player == "L":
            self.l_score += 1
            self._writea("LEFT SCORES!")
        else:
            self.r_score += 1
            self._writea("RIGTH SCORES!")

    def game_over(self):
        """Display the game over message."""
        self.goto(0, 0)
        self._writea("GAME OVER")

    def _writea(self, text):
        """Write text to the screen."""
        self.write(text, align=ALIGNMENT, font=FONT)
