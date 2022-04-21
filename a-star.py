import const
from action import Action
from state import State


# cost function
def heuristic(start, end):
    (x1, y1) = (start.x, start.y)
    (x2, y2) = end
    distance = abs(x2 - x1) + abs(y2 - y1)

    return distance


def a_star_search(start_state: State, end):
    open_list = [start_state] # list of visited states but the neighbours not fully inspected
    distances = {start_state: 0} # dictionary of distances from start
    closed_list = [] # list of visited states with fully inspected neighbours
    nodes_map = {start_state: start_state} # dictionary of mapped states

    while len(open_list) > 0:
        current_state = None
        for state in open_list:
            # looking for states with lowest cost
            if current_state is None or (distances[state] + heuristic(state, end) < distances[current_state] + heuristic(current_state, end)):
                current_state = state

        if current_state is None:
            return None

        if (current_state.x, current_state.y) == end: # if current state is the end path is reconstructed using parents
            path = []

            while current_state is not start_state:
                path.append(current_state.action)
                current_state = current_state.parent

            path.reverse()
            return path

        # checking current state neighbours
        for neighbour in current_state.get_neighbours():
            if neighbour not in open_list and neighbour not in closed_list: # if its completely new state
                open_list.append(neighbour)
                neighbour.parent = current_state
                distances[neighbour] = neighbour.weight + distances[current_state]
            else:
                if distances[neighbour] > distances[current_state] + neighbour.weight: # if its quicker to move with current state than neighbour we have to update its data
                    distances[neighbour] = distances[current_state] + neighbour.weight
                    neighbour.parent = current_state

                    if neighbour in closed_list: # if neighbour was in closed list we have to move it to open list
                        closed_list.remove(neighbour)
                        open_list.append(neighbour)

        open_list.remove(current_state) # end of the loop, adding current state to closed list
        closed_list.append(current_state)

    return None


# test
print(a_star_search(start_state=State(const.START_POS, Action.NONE), end=(24, 20)))