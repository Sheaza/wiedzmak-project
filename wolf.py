from monster import Monster


class Wolf(Monster):
    counter = 0

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\wilk.png')
        self.image = "zdjecie z setu danych"
        self.effective_oil = "oil_beast"
        self.effective_sword = "sword_silver"

        Wolf.counter += 1
        print("spawned wolf", Wolf.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("wilk")

    def set_image(self):
        self.image = "zdjecie z setu danych"
