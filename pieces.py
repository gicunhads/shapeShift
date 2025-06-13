from enum import Enum

class Color(Enum):
    BLACK = 'Black'
    WHITE = 'White'

class Shape(Enum):
    HEART = 'Heart'
    TRIANGLE = 'Triangle'

class Size(Enum):
    BIG = 'Big'
    SMALL = 'Small'

class Piece:
    def __init__(self, color: Color, shape: Shape, size: Size):
        self.color = color
        self.shape = shape
        self.size = size

    def __repr__(self):
        return f"{self.color.value[0]}-{self.shape.value[0]}-{self.size.value[0]}"
