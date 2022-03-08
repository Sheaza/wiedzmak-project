import const
from pygame import draw


class Grid:
    def draw_grid(self, window):
        for i in range(int(const.rows)):
            draw.line(window, const.LINES, (0, i * const.GAP), (const.windows_size[0], i * const.GAP))
            for j in range(int(const.columns)):
                draw.line(window, const.LINES, (j * const.GAP, 0), (j * const.GAP, const.windows_size[1]))
