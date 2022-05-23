from monster import Monster
from oils import Oil
from swords import Sword


class Wolf(Monster):
    counter = 0

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\wilk.png')
        self.image = "zdjecie z setu danych"
        self.effective_oil = Oil.BEAST
        self.effective_sword = Sword.STEEL
        self.attributes = [1,0,1,1,0,1,0,0] #'pazury', 'skrzydla', 'ogon', 'siersc', 'dwie nogi', 'kly', 'rogi', 'humanoidalnosc'

        Wolf.counter += 1
        print("spawned wolf", Wolf.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("wilk")

    def set_image(self):
        self.image = "zdjecie z setu danych"
