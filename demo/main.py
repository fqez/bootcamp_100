import random
from turtle import Turtle, Screen

# Constants
STEP = 5
COLORS = [
    "red",
    "green",
    "blue",
    "orange",
    "pink",
    "magenta",
    "cyan",
    "yellow",
    "purple",
    "brown",
    "white",
    "gray",
    "lightblue",
    "lime",
    "teal",
    "olive",
    "maroon",
    "navy",
    "silver",
]
WIDTH = 800
HEIGHT = 600
OFFSET = 150
FINISH_LINE = WIDTH // 2 - OFFSET
START_X = -350
NUM_RUNNERS = 5


class Runner(Turtle):
    def __init__(self, color, start_y):
        super().__init__(shape="turtle")
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.teleport(START_X, start_y)


class TurtleRace:
    def __init__(self, num_runners=NUM_RUNNERS):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.user_bet = self.screen.textinput(
            title="Make your bet!",
            prompt="Which turtle will win the race? (choose the color): ",
        )
        self.create_referee()
        self.runners = self.create_runners(num_runners)

    def create_runners(self, n):
        start = HEIGHT // 2 - OFFSET
        step = (start * 2) // n
        return [Runner(COLORS[i], start - (i * step)) for i in range(n)]

    def create_referee(self):
        referee = Turtle(shape="turtle")
        referee.color("black")
        referee.teleport(x=FINISH_LINE, y=WIDTH // 2 - OFFSET)
        referee.setheading(270)
        referee.forward(HEIGHT - OFFSET)
        referee.setheading(90)

    def check_winner(self, runner):
        if runner.xcor() > FINISH_LINE:
            winning_color = runner.pencolor()
            if winning_color == self.user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            return True
        return False

    def start_race(self):
        while True:
            for runner in self.runners:
                if self.check_winner(runner):
                    return
                runner.forward(random.randint(0, STEP))


def main():
    race = TurtleRace()
    race.start_race()


if __name__ == "__main__":
    main()
