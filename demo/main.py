import random
import turtle as t
from enum import Enum
import colorgram


# Iterator not needed, but just for trying
COLOURS: list[str] = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
DIRECTIONS = [0, 90, 180, 270]  # East, North, West, South


class SHAPES(Enum):
    TRIANGLE = 3
    SQUARE = 4
    PENTAGON = 5
    HEXAGON = 6
    HEPTAGON = 7
    OCTAGON = 8
    NONAGON = 9
    DECAGON = 10


def generate_random_color():

    # return (random.randrange(0, 255) / 255, random.randint(0,255) / 255, random.randint(0,255) /255)
    return (random.randrange(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_shape(sides: SHAPES, artist: t.Turtle) -> None:
    """
    Draw a shape with the given number of sides using the turtle.
    """
    angle = int(360 / sides.value)
    for _ in range(sides.value):
        artist.forward(100)
        artist.right(angle)


def random_walk(steps: int, artist: t.Turtle) -> None:
    """
    Perform a random walk with the turtle for the given number of steps.
    """

    for _ in range(steps):
        direction = random.choice(DIRECTIONS)
        artist.color(generate_random_color())
        artist.setheading(direction)
        artist.forward(50)


def draw_spirograph(gap: int, artist: t.Turtle) -> None:

    offset = 360 / gap
    for i in range(gap):
        artist.color(generate_random_color())
        artist.circle(100)
        artist.seth(artist.heading() + offset)


def modern_artist(artist: t.Turtle, size: int = 10, dot_size: int = 20):

    colors = colorgram.extract("image.jpg", 15)

    for i in range(size * size):
        x = i // size
        y = i % size
        color = random.choice(colors).rgb
        artist.dot(dot_size, color)
        artist.teleport(y * (dot_size * 2), x * (dot_size * 2))


if __name__ == "__main__":

    espartaco = t.Turtle()
    screen = t.Screen()

    espartaco.shape("turtle")
    espartaco.pensize(8)
    espartaco.speed("fastest")

    screen.colormode(255)

    # Uncomment the following lines to draw shapes
    # colors = colorgram.extract('image.jpg', 10)
    # for shape in SHAPES:
    #     espartaco.color(random.choice(colors).rgb)
    #     draw_shape(shape, espartaco)

    # random_walk(250, espartaco)

    # draw_spirograph(100, espartaco)

    modern_artist(artist=espartaco)

    screen.exitonclick()
