from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Fira Code", 14, "bold")
INITIAL_SCORE_POSITION = (0, 270)


class Scoreboard(Turtle):
    """A class representing the game scoreboard."""

    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()

        self._score = 0

        self.color("white")
        self.penup()
        self.goto(INITIAL_SCORE_POSITION)
        self.hideturtle()
        self._writea(f"Score: {self._score}")

    @property
    def score(self):
        """The current score."""
        return self._score

    @score.setter
    def score(self, value):
        """Set the score and update the display."""
        self._score = value
        self.update_score()

    def update_score(self):
        """Update the score display."""
        self._score += 1
        self.clear()
        self._writea(f"Score: {self._score}")

    def game_over(self):
        """Display the game over message."""
        self.goto(0, 0)
        self._writea("GAME OVER")

    def _writea(self, text):
        """Write text to the screen."""
        self.write(text, align=ALIGNMENT, font=FONT)
