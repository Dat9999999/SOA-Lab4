from enum import Enum
class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    PINK = "pink"
    WHITE = "white"
    BLACK = "black"
    ORANGE = "orange"

def is_valid_color(val):
    return val in Color.__members__.values()
