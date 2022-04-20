class Camera:

    def update_map_square(self, pos_x, pos_y):
        # Moving camera on x axis
        if pos_x < 16:
            map_x = 0
        elif 16 <= pos_x < 32:
            map_x = 1
        elif pos_x >= 32:
            map_x = 2

        # Moving camera on y axis
        if pos_y < 16:
            map_y = 0
        elif 16 <= pos_y < 32:
            map_y = 1
        elif pos_y >= 32:
            map_y = 2

        return map_x, map_y