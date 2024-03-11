import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(fun=player.move, key="Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)

        if car_manager.check_collisions(player):
            game_is_on = False
            scoreboard.game_over()

        if player.check_won():
            car_manager.new_level()
            scoreboard.increment_level()

        car_manager.move_cars()
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
