from turtle import pos
from typing import Tuple, List
from action import Action
from grid import Grid
from orientation import Orientation


class State:
    def __init__(self, position, orientation):
        self.pos = position # unpacking the position tuple
        self.orientation = orientation
        self.x, self.y = position

    def __eq__(self, other) -> bool:
        return other.pos == self.pos and self.orientation == other.orientation

    def __lt__(self, state):
        return self.pos < state.pos

    def __hash__(self) -> int:
        return hash(self.orientation)
