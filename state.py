from turtle import pos
from typing import Tuple, List
from action import Action
from grid import Grid
from orientation import Orientation


class State:
    def __init__(self, position, action):
        self.x, self.y, self.orientation = position # unpacking the position tuple
        self.action = action # which action was performed

        if action in [Action.MOVE_UP, Action.MOVE_DOWN, Action.MOVE_RIGHT, Action.MOVE_LEFT]:  # just to see if it works TODO: add map dependecy
            self.weight = 1
        else:
            self.weight = 0

    def get_neighbours(self, grid=Grid()): # taking the grid to check collisions
        x = self.x
        y = self.y
        results = []
        orientation = self.orientation

        if orientation == Orientation.UP: # adding to result list possible states other elifs do the same
            results = [State((x, y, Action.TURN_LEFT.value), Action.TURN_LEFT),
                       State((x, y, Action.TURN_RIGHT.value), Action.TURN_RIGHT),
                       State((x, y, Action.TURN_DOWN.value), Action.TURN_DOWN)]

            action_x, action_y = Action.MOVE_UP.value
            if (x + action_x, y + action_y) in grid.nodes: # checking if wiedzmak can move in this direction idk if it works
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE_UP))

        elif orientation == Orientation.DOWN:
            results = [State((x, y, Action.TURN_LEFT.value), Action.TURN_LEFT),
                       State((x, y, Action.TURN_RIGHT.value), Action.TURN_RIGHT),
                       State((x, y, Action.TURN_UP.value), Action.TURN_UP)]

            action_x, action_y = Action.MOVE_DOWN.value
            if (x + action_x, y + action_y) in grid.nodes:
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE_DOWN))

        elif orientation == Orientation.LEFT:
            results = [State((x, y, Action.TURN_UP.value), Action.TURN_UP),
                       State((x, y, Action.TURN_RIGHT.value), Action.TURN_RIGHT),
                       State((x, y, Action.TURN_DOWN.value), Action.TURN_DOWN)]

            action_x, action_y = Action.MOVE_LEFT.value
            if (x + action_x, y + action_y) in grid.nodes:
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE_LEFT))

        elif orientation == Orientation.RIGHT:
            results = [State((x, y, Action.TURN_LEFT.value), Action.TURN_LEFT),
                       State((x, y, Action.TURN_UP.value), Action.TURN_UP),
                       State((x, y, Action.TURN_DOWN.value), Action.TURN_DOWN)]

            action_x, action_y = Action.MOVE_RIGHT.value
            if (x + action_x, y + action_y) in grid.nodes:
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE_RIGHT))
        return results
