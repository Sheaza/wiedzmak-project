from monster import Monster


class Griffin(Monster):
    counter = 0

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\gryf.png')
        self.image = "zdjecie z setu danych"
        self.effective_oil = "oil_hybrid"
        self.effective_sword = "sword_silver"

        Griffin.counter += 1
        print("spawned griffin", Griffin.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("gryf")

    def set_image(self):
        self.image = "zdjecie z setu danych"
