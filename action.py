from enum import Enum
from orientation import Orientation


class Action(Enum):
    NONE = 0
    MOVE_UP = [0, 1]
    MOVE_DOWN = [0, -1]
    MOVE_LEFT = [-1, 0]
    MOVE_RIGHT = [1, 0]
    TURN_UP = Orientation.UP
    TURN_DOWN = Orientation.DOWN
    TURN_LEFT = Orientation.LEFT
    TURN_RIGHT = Orientation.RIGHT
