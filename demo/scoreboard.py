from turtle import Turtle
from typing import Tuple

ALIGNMENT = "center"
FONT = ("Fira Code", 14, "bold")
INITIAL_SCORE_POSITION: Tuple[int, int] = (-100, 270)
HIGHSCORE_FILE: str = "highscore.txt"


class Scoreboard(Turtle):
    """
    A class representing the scoreboard in a game.
    """

    def __init__(self):
        super().__init__()

        self._score: int = -1
        self._highscore: int = self.load_highscore()

        self.color("white")
        self.penup()
        self.goto(INITIAL_SCORE_POSITION)
        self.hideturtle()
        self.update_score()

    @property
    def score(self) -> int:
        """
        Get the current score.
        """
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        """
        Set the current score.
        """
        self._score = value
        self.update_score()

    @property
    def highscore(self) -> int:
        """
        Get the high score.
        """
        return self._highscore

    @highscore.setter
    def highscore(self, value: int) -> None:
        """
        Set the high score.
        """
        self._highscore = value

    def update_score(self) -> None:
        """
        Update the score by incrementing it by 1 and displaying it.
        """
        self.clear()
        self._score += 1
        self.write_score()

    def reset(self) -> None:
        """
        Reset the scoreboard.
        If the current score is higher than the high score, save it as the new high score.
        """
        if self.is_new_highscore():
            self.save_highscore()
        self.score = -1

    def load_highscore(self) -> int:
        """
        Load the high score from a file.
        """
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read())

    def save_highscore(self) -> None:
        """
        Save the current score as the new high score in a file.
        """
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(self.score))

    def is_new_highscore(self) -> bool:
        """
        Check if the current score is higher than the high score.
        """
        return self.score > self.highscore

    def write_score(self) -> None:
        """
        Write the current score and high score on the screen.
        """
        self._writea(f"Score: {self.score}\t High Score: {self.highscore}")

    def _writea(self, text: str) -> None:
        """
        Write the given text on the screen.
        """
        self.write(text, align=ALIGNMENT, font=FONT)
