import time
from turtle import Screen, Turtle

from ball import Ball
from constants import (
    BALL_OFFSET,
    GOAL_OFFSET,
    HEIGHT,
    PADDLE_OFFSET,
    WIDTH,
    WIDTH_OFFSET,
)
from paddle import Paddle
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        """
        Initialize the game.
        """
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.title("Pong")

        self.fps = 30

        self.r_paddle = Paddle((WIDTH // 2 - WIDTH_OFFSET, 0))
        self.l_paddle = Paddle((-WIDTH // 2 + WIDTH_OFFSET, 0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.init_game_control_bindings()
        self.draw_dashed_line()

    def draw_dashed_line(self):
        """
        Draw a vertical dashed line in the middle of the screen from top to bottom.
        """
        dashed_turtle = Turtle()
        dashed_turtle.penup()
        dashed_turtle.goto(0, HEIGHT // 2)  # Start at the top of the screen
        dashed_turtle.setheading(270)  # Point the turtle downwards
        dashed_turtle.pendown()
        dashed_turtle.pensize(3)
        dashed_turtle.color("white")

        for _ in range(HEIGHT // 20):
            # Adjust the range based on the height of the screen and the length of the dashes
            dashed_turtle.forward(10)
            dashed_turtle.penup()
            dashed_turtle.forward(10)
            dashed_turtle.pendown()

        dashed_turtle.hideturtle()

    def game_start(self):
        """
        Start the game loop.
        """
        frame_delay = 1.0 / self.fps  # Calculate the delay for each frame

        while True:

            start_time = time.time()  # Record the start time of the frame

            self.ball.move()
            self.detect_collision()
            if self.detect_goal():
                self.ball.reset_position()
                self.screen.update()
                time.sleep(1)
                self.scoreboard.update_score()

            self.screen.update()
            # Calculate how long the frame took to process
            frame_time = time.time() - start_time

            # If the frame finished faster than the desired frame time, sleep the remaining time
            if frame_time < frame_delay:
                time.sleep(frame_delay - frame_time)

    def detect_goal(self):
        if self.ball.xcor() > WIDTH // 2 - GOAL_OFFSET:
            self.scoreboard.point("L")
            return True

        if self.ball.xcor() < -WIDTH // 2 + GOAL_OFFSET:
            self.scoreboard.point("R")
            return True

        return False

    def detect_collision(self):

        # detect collision with top or bottom
        if (
            self.ball.ycor() > HEIGHT // 2 - BALL_OFFSET
            or self.ball.ycor() < -HEIGHT // 2 + BALL_OFFSET
        ):
            self.ball.bounce_y()

        if (
            self.ball.distance(self.r_paddle) < 50
            and self.ball.xcor() > WIDTH // 2 - PADDLE_OFFSET
        ) or (
            self.ball.distance(self.l_paddle) < 50
            and self.ball.xcor() < -WIDTH // 2 + PADDLE_OFFSET
        ):
            self.ball.bounce_x()

    def init_game_control_bindings(self):
        """Initialize game control bindings."""
        self.screen.listen()
        key_mapping = {
            "Up": self.r_paddle.go_up,
            "Down": self.r_paddle.go_down,
            "w": self.l_paddle.go_up,
            "s": self.l_paddle.go_down,
            "q": self.screen.bye,
        }
        for key, fnct in key_mapping.items():
            self.screen.onkeypress(fun=fnct, key=key)


def main():
    """
    Main function to start the game.
    """
    pong = Game()
    pong.game_start()
    pong.screen.exitonclick()


if __name__ == "__main__":
    main()
