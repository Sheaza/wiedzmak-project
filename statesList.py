from sqlite3 import paramstyle
from typing import List
from grid import Grid
from orientation import Orientation
from action import Action
from state import State
import const

class StatesList():
    def __init__(self) -> None:
        self.parent = State(Action.NONE, const.START_POS)
    
    def neighbours(self, parent: State, grid=Grid()) -> List[State]:
        action = parent.action
        x = parent.x
        y = parent.y
        results = []
        orientation = parent.orientation
        if orientation == Orientation.UP:
            results = [State(Action.TURN_LEFT (x, y, Action.TURN_LEFT)), State(Action.TURN_RIGHT (x, y, Action.TURN_RIGHT)), State(Action.TURN_DOWN (x, y, Action.TURN_DOWN))]
            if (x + Action.MOVE_UP[0], y + Action.MOVE_UP[1]) in grid.nodes:
                results.append(State(Action.MOVE_UP (x + Action.MOVE_UP[0], y + Action.MOVE_UP[1], orientation)))

        elif orientation == Orientation.DOWN:
            results = [State(Action.TURN_LEFT (x, y, Action.TURN_LEFT)), State(Action.TURN_RIGHT (x, y, Action.TURN_RIGHT)), State(Action.TURN_UP (x, y, Action.TURN_UP))]
            if (x + Action.MOVE_DOWN[0], y + Action.MOVE_DOWN[1]) in grid.nodes:
                results.append(State(Action.MOVE_DOWN, (x + Action.MOVE_DOWN[0], y + Action.MOVE_DOWN[1], orientation)))
        elif orientation == Orientation.LEFT:
            results = [State(Action.TURN_UP (x, y, Action.TURN_UP)), State(Action.TURN_RIGHT (x, y, Action.TURN_RIGHT)), State(Action.TURN_DOWN (x, y, Action.TURN_DOWN))]
            if (x + Action.MOVE_LEFT[0], y + Action.MOVE_LEFT[1]) in grid.nodes:
                results.append(State(Action.MOVE_LEFT, (x + Action.MOVE_LEFT[0], y + Action.MOVE_LEFT[1], orientation)))
        elif orientation == Orientation.RIGHT:
            results = [State(Action.TURN_LEFT, (x, y, Action.TURN_LEFT)), State(Action.TURN_UP (x, y, Action.TURN_UP)), State(Action.TURN_DOWN (x, y, Action.TURN_DOWN))]
            if (x + Action.MOVE_RIGHT[0], y + Action.MOVE_RIGHT[1]) in grid.nodes:
                results.append(State(Action.MOVE_RIGHT, (x + Action.MOVE_RIGHT[0], y + Action.MOVE_RIGHT[1], orientation)))
        return results
