from __future__ import annotations
from typing import Optional

import const
from action import Action
from grid import Grid
from state import State


class Node:
    def __init__(self, state: State, parent: Optional[Node], action: Optional[Action]):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0
        if self.state.pos not in const.COLLISIONS and self.state.pos not in const.ROCKS and self.state.pos not in const.WATER:
            self.cost = 1 if not self.parent else self.parent.cost + 1
        elif self.state.pos in const.WATER:
            self.cost = 10 if not self.parent else self.parent.cost + 10
        elif self.state.pos in const.ROCKS:
            self.cost = 3 if not self.parent else self.parent.cost + 3

    def __lt__(self, node) -> None:
        return self.state < node.state

    def __hash__(self) -> int:
        return hash(self.state)

