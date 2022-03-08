class Camera:

    def update_camera(self, pos_x, pos_y):
        if pos_x < 16:
            camera_x = 0
        elif 16 <= pos_x < 32:
            camera_x = -800
        elif pos_x >= 32:
            camera_x = -1600

        # Moving camera on y axis
        if pos_y < 16:
            camera_y = 0
        elif 16 <= pos_y < 32:
            camera_y = -800
        elif pos_y >= 32:
            camera_y = -1600

        return camera_x, camera_y