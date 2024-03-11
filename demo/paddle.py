from enum import Enum
from turtle import Turtle

from constants import HEIGHT, HEIGHT_OFFSET, PADDLE_SPEED


class DIRECTIONS(Enum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        if self.ycor() < HEIGHT // 2 - HEIGHT_OFFSET:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def go_down(self):
        if self.ycor() > -HEIGHT // 2 + HEIGHT_OFFSET:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)
