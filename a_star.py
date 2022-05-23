import heapq

import const
from action import Action
from grid import Grid
from node import Node
from orientation import Orientation
from state import State


def nearest_monster_pos(witcher_pos, monsters_pos):
    nearest_pos = None
    shortest_dist = float("inf")
    for monster_pos in monsters_pos:
        current_dist = calculate_distance(witcher_pos, monster_pos)
        if current_dist < shortest_dist:
            nearest_pos = monster_pos
            shortest_dist = current_dist

    return nearest_pos


def calculate_distance(start, end):
    (x1, y1) = start
    (x2, y2) = end
    distance = abs(x2 - x1) + abs(y2 - y1)

    return distance


# cost function
def heuristic(start, end):
    (x1, y1) = start.pos
    (x2, y2) = end
    distance = abs(x2 - x1) + abs(y2 - y1)

    return distance


def f(node: Node, end):
    return node.cost + heuristic(start=node.state, end=end)


def get_neighbours(node: Node):
    return [neighbour(node=node, action=action) for action in actions(node.state)]


def actions(state: State, grid=Grid()):
    possible = [Action.MOVE, Action.TURN_RIGHT, Action.TURN_LEFT]
    x, y = state.pos
    orientation = state.orientation

    if orientation == Orientation.UP and (x, y - 1) not in grid.nodes:
        possible.remove(Action.MOVE)
    if orientation == Orientation.DOWN and (x, y + 1) not in grid.nodes:
        possible.remove(Action.MOVE)
    if orientation == Orientation.LEFT and (x - 1, y) not in grid.nodes:
        possible.remove(Action.MOVE)
    if orientation == Orientation.RIGHT and (x + 1, y) not in grid.nodes:
        possible.remove(Action.MOVE)

    return possible


def neighbour(node: Node, action: Action, grid=Grid()):
    next = get_next(state=node.state, action=action)
    return Node(state=next, parent=node, action=action)


def get_next(state: State, action: Action):
    next = State(state.pos, state.orientation)

    if state.orientation == Orientation.UP:
        if action == Action.TURN_LEFT:
            next.orientation = Orientation.LEFT
        elif action == Action.TURN_RIGHT:
            next.orientation = Orientation.RIGHT
        elif action == Action.MOVE:
            next.pos = next.x, next.y - 1

    if state.orientation == Orientation.DOWN:
        if action == Action.TURN_LEFT:
            next.orientation = Orientation.LEFT
        elif action == Action.TURN_RIGHT:
            next.orientation = Orientation.RIGHT
        elif action == Action.MOVE:
            next.pos = next.x, next.y + 1

    if state.orientation == Orientation.LEFT:
        if action == Action.TURN_LEFT:
            next.orientation = Orientation.DOWN
        elif action == Action.TURN_RIGHT:
            next.orientation = Orientation.UP
        elif action == Action.MOVE:
            next.pos = next.x - 1, next.y

    if state.orientation == Orientation.RIGHT:
        if action == Action.TURN_RIGHT:
            next.orientation = Orientation.DOWN
        elif action == Action.TURN_LEFT:
            next.orientation = Orientation.UP
        elif action == Action.MOVE:
            next.pos = next.x + 1, next.y
    return next


def a_star_search(start_state: State, end):
    node = Node(state=start_state, parent=None, action=None)
    fringe = list()
    heapq.heappush(fringe, (f(node, end), node))
    visited = set()

    while fringe:
        w, node = heapq.heappop(fringe)

        if node.state.pos == end:
            path = [node.action]

            while node.parent is not None:
                node = node.parent
                path.append(node.action)
            path.reverse()
            path.pop(0)
            return path

        visited.add(node.state)

        for n in get_neighbours(node):
            cost = f(n, end)
            if n.state not in visited and (cost, n) not in fringe:
                heapq.heappush(fringe, (cost, n))
            elif (w, n) in fringe and w > cost:
                heapq.heappush(fringe, (cost, n))

    return []


# test
print(a_star_search(start_state=State(const.START_POS, const.START_ORIENTATION), end=(13,12)))