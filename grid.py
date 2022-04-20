import const
from pygame import draw


class Grid:
    def __init__(self):
        self.nodes = []
        for x in range(const.GRID_SIZE):
            for y in range(const.GRID_SIZE):
                node = (x, y)
                if node not in const.COLLISIONS:
                    self.nodes.append(node)

    def draw_grid(self, window):
        for i in range(int(const.rows)):
            draw.line(window, const.LINES, (0, i * const.GAP), (const.windows_size[0], i * const.GAP))
            for j in range(int(const.columns)):
                draw.line(window, const.LINES, (j * const.GAP, 0), (j * const.GAP, const.windows_size[1]))

