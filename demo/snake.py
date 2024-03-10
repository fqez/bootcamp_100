from enum import Enum
from turtle import Turtle

SEGMENT_SIZE = 20


class DIRECTIONS(Enum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


class Piece(Turtle):
    def __init__(self, pos_x=None, pos_y=None, position=None):
        super().__init__(shape="square")
        self.color("green")
        self.penup()
        if position:
            self.goto(x=position[0], y=position[1])
        else:
            self.goto(x=pos_x, y=pos_y)


class Snake:
    """A class representing the snake."""

    OPPOSITE_DIRECTIONS = {
        DIRECTIONS.UP: DIRECTIONS.DOWN,
        DIRECTIONS.DOWN: DIRECTIONS.UP,
        DIRECTIONS.LEFT: DIRECTIONS.RIGHT,
        DIRECTIONS.RIGHT: DIRECTIONS.LEFT,
    }

    def __init__(self):
        """Initialize the snake."""
        self.segments = [
            self._create_piece(pos_x=-i * SEGMENT_SIZE, pos_y=0) for i in range(3)
        ]
        self.head.color("lightgreen")

    @property
    def head(self):
        """The head of the snake."""
        return self.segments[0]

    def move(self):
        """Move the snake forward."""
        for seg, next_seg in zip(self.segments[::-1], self.segments[-2::-1]):
            seg.goto(next_seg.position())
        self.head.forward(SEGMENT_SIZE)

    def change_direction(self, new_direction):
        """Change the direction of the snake."""
        if self.head.heading() != self.OPPOSITE_DIRECTIONS[new_direction].value:
            self.head.setheading(new_direction.value)

    def create_new_piece(self):
        """Add a new piece to the snake."""
        self.segments.append(self._create_piece(position=self.segments[-1].position()))

    def _create_piece(self, pos_x=0, pos_y=0, position=None):
        """Create a new piece."""
        return Piece(pos_x=pos_x, pos_y=pos_y, position=position)
