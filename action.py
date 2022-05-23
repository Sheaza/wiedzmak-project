from enum import Enum
from orientation import Orientation


class Action(Enum):
    NONE = 0
    MOVE = 1
    TURN_UP = Orientation.UP
    TURN_DOWN = Orientation.DOWN
    TURN_LEFT = Orientation.LEFT
    TURN_RIGHT = Orientation.RIGHT