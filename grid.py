import const
from collections import deque
from pygame import draw


class Grid:
    def __init__(self):
        self.nodes = []
        for x in range(const.GRID_SIZE):
            for y in range(const.GRID_SIZE):
                node = (x,y)
                if node not in const.COLLISIONS:
                    self.nodes.append(node)

    def get_path(self, start, goal):
        explored_from = self.breadth_first_search(start, goal)
        path = []
        current = goal

        while current != start:
            path.append(current)
            current = explored_from[current]
        path.reverse()

        return path

    def breadth_first_search(self, start, goal):
        queue = deque()
        queue.append(start)
        explored_from = dict()
        explored_from[start] = None

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            for neighbor in self.neighbors(current):
                if neighbor not in explored_from:
                    queue.append(neighbor)
                    explored_from[neighbor] = current

        return explored_from

    def neighbors(self, node):
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        result = []
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if neighbor in self.nodes:
                result.append(neighbor)
        return result

    def draw_grid(self, window):
        for i in range(int(const.rows)):
            draw.line(window, const.LINES, (0, i * const.GAP), (const.windows_size[0], i * const.GAP))
            for j in range(int(const.columns)):
                draw.line(window, const.LINES, (j * const.GAP, 0), (j * const.GAP, const.windows_size[1]))
