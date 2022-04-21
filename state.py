from turtle import pos
from typing import Tuple, List
from action import Action
from grid import Grid
from orientation import Orientation


class State:
    def __init__(self, position, action):
        self.x, self.y, self.orientation = position # unpacking the position tuple
        self.action = action # which action was performed
        self.parent = None # parent of the state

        if action == Action.MOVE:  # just to see if it works TODO: add map dependecy
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
                       State((x, y, Action.TURN_RIGHT.value), Action.TURN_RIGHT)]

            action_x, action_y = 0, 1
            if (x + action_x, y + action_y) in grid.nodes: # checking if wiedzmak can move in this direction idk if it works
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE))

        elif orientation == Orientation.DOWN:
            results = [State((x, y, Action.TURN_LEFT.value), Action.TURN_LEFT),
                       State((x, y, Action.TURN_RIGHT.value), Action.TURN_RIGHT)]

            action_x, action_y = 0, -1
            if (x + action_x, y + action_y) in grid.nodes:
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE))

        elif orientation == Orientation.LEFT:
            results = [State((x, y, Action.TURN_UP.value), Action.TURN_UP),
                       State((x, y, Action.TURN_DOWN.value), Action.TURN_DOWN)]

            action_x, action_y = -1, 0
            if (x + action_x, y + action_y) in grid.nodes:
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE))

        elif orientation == Orientation.RIGHT:
            results = [State((x, y, Action.TURN_UP.value), Action.TURN_UP),
                       State((x, y, Action.TURN_DOWN.value), Action.TURN_DOWN)]

            action_x, action_y = 1, 0
            if (x + action_x, y + action_y) in grid.nodes:
                results.append(State((x + action_x, y + action_y, orientation), Action.MOVE))
        return results
