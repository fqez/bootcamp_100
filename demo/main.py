import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import DIRECTIONS, Snake

# Constants
WIDTH = 600
HEIGHT = 600
SEGMENT_SIZE = 20

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game!🐍")

fps = 12
snake = Snake()
food = Food(WIDTH, HEIGHT)
scoreboard = Scoreboard()


def check_food():
    return True if snake.head.distance(food.pos()) <= 15 else False


def check_collision():
    xc, yc = snake.head.xcor(), snake.head.ycor()
    horizontal_border = WIDTH // 2 - SEGMENT_SIZE
    vertical_border = HEIGHT // 2 - SEGMENT_SIZE

    if abs(xc) > horizontal_border or abs(yc) > vertical_border:
        return True

    return any(snake.head.distance(segment) < 10 for segment in snake.segments[1:])


def game_start():
    frame_delay = 1.0 / fps  # Calculate the delay for each frame

    while True:
        start_time = time.time()  # Record the start time of the frame

        snake.move()
        if check_collision():
            scoreboard.reset()
            snake.reset()
            screen.update()

        if check_food():
            scoreboard.update_score()
            food.create_new()
            snake.create_new_piece()
        screen.update()

        # Calculate how long the frame took to process
        frame_time = time.time() - start_time

        # If the frame finished faster than the desired frame time, sleep the remaining time
        if frame_time < frame_delay:
            time.sleep(frame_delay - frame_time)


def init_game_control_bindings():
    screen.listen()
    key_mapping = {
        "Up": DIRECTIONS.UP,
        "Down": DIRECTIONS.DOWN,
        "Left": DIRECTIONS.LEFT,
        "Right": DIRECTIONS.RIGHT,
    }
    for key, direction in key_mapping.items():
        screen.onkey(fun=lambda dir=direction: snake.change_direction(dir), key=key)


init_game_control_bindings()
game_start()
screen.exitonclick()
