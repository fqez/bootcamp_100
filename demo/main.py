import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import DIRECTIONS, Snake

# Constants
WIDTH = 600
HEIGHT = 600
SEGMENT_SIZE = 20


class Game:
    def __init__(self):
        """
        Initialize the game.
        """
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game!🐍")

        self.fps = 12

        self.init_game_control_bindings()

        self.snake = Snake()
        self.food = Food(WIDTH, HEIGHT)
        self.scoreboard = Scoreboard()

    @property
    def check_food(self) -> bool:
        """
        Check if the snake has reached the food.
        Returns:
            bool: True if the snake has reached the food, False otherwise.
        """
        return True if self.snake.head.distance(self.food.pos()) <= 15 else False

    @property
    def check_collision(self):
        """Check if the snake has collided with the border or its tail."""
        xc, yc = self.snake.head.xcor(), self.snake.head.ycor()
        horizontal_border = WIDTH // 2 - SEGMENT_SIZE
        vertical_border = HEIGHT // 2 - SEGMENT_SIZE

        if abs(xc) > horizontal_border or abs(yc) > vertical_border:
            return True

        return any(
            self.snake.head.distance(segment) < 10
            for segment in self.snake.segments[1:]
        )

    def game_start(self):
        """
        Start the game loop.
        """
        frame_delay = 1.0 / self.fps  # Calculate the delay for each frame

        while True:

            start_time = time.time()  # Record the start time of the frame

            self.snake.move()
            if self.check_collision:
                self.scoreboard.game_over()
                break

            if self.check_food:
                self.scoreboard.update_score()
                self.food.create_new()
                self.snake.create_new_piece()
            self.screen.update()

            # Calculate how long the frame took to process
            frame_time = time.time() - start_time

            # If the frame finished faster than the desired frame time, sleep the remaining time
            if frame_time < frame_delay:
                time.sleep(frame_delay - frame_time)

    def init_game_control_bindings(self):
        """Initialize game control bindings."""
        self.screen.listen()
        key_mapping = {
            "Up": DIRECTIONS.UP,
            "Down": DIRECTIONS.DOWN,
            "Left": DIRECTIONS.LEFT,
            "Right": DIRECTIONS.RIGHT,
        }
        for key, direction in key_mapping.items():
            self.screen.onkey(
                fun=lambda dir=direction: self.snake.change_direction(dir), key=key
            )


def main():
    """
    Main function to start the game.
    """
    snake = Game()
    snake.game_start()
    snake.screen.exitonclick()


if __name__ == "__main__":
    main()
