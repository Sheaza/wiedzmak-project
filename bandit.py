from monster import Monster


class Bandit(Monster):
    counter = 0

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\bandyta.png')
        self.image = "zdjecie z setu danych"
        self.effective_oil = "oil_kujawski"
        self.effective_sword = "sword_steel"

        Bandit.counter += 1
        print("spawned bandit", Bandit.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("bandyta")

    def set_image(self):
        self.image = "zdjecie z setu danych"
