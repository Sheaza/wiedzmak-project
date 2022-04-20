from monster import Monster


class Leshy(Monster):
    counter = 0
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\leszy.png')
        self.image = "zdjecie z setu danych"
        self.effective_oil = "oil_relict"
        self.effective_sword = "sword_silver"

        Leshy.counter += 1
        print("spawned leshy", Leshy.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("leszy")

    def set_image(self):
        self.image = "zdjecie z setu danych"
