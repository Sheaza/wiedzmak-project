from monster import Monster


class Leszy(Monster):
    counter = 0

    def __init__(self, x, y):
        self.set_image()
        self.asset = "leszy asset"
        self.pos_x = x
        self.pos_y = y
        Leszy.counter += 1
        print("spawned leszy", Leszy.counter)

    def sendImg(self):
        print("leszy")

    def set_image(self):
        self.image = "zdjecie z setu danych"
