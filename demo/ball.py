from turtle import Turtle


class Ball(Turtle):
    """A class representing the food in the game."""

    def __init__(self):
        """Initialize the food."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dir_x = 1
        self.dir_y = 1
        self.ball_speed = 5

    def move(self):
        self.goto(
            x=self.xcor() + self.ball_speed * self.dir_x,
            y=self.ycor() + self.ball_speed * self.dir_y,
        )

    def bounce_y(self):
        self.dir_y *= -1

    def bounce_x(self):
        self.dir_x *= -1
        self.ball_speed += 0.5

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 5
