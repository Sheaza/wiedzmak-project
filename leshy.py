from monster import Monster
from oils import Oil
from swords import Sword


class Leshy(Monster):
    counter = 0
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\leszy.png')
        self.image = "zdjecie z setu danych"
        self.effective_oil = Oil.RELICT
        self.effective_sword = Sword.SILVER
        self.attributes = [1,0,0,0,1,0,1,2] #'pazury', 'skrzydla', 'ogon', 'siersc', 'dwie nogi', 'kly', 'rogi', 'humanoidalnosc'

        Leshy.counter += 1
        print("spawned leshy", Leshy.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("leszy")

    def set_image(self):
        self.image = "zdjecie z setu danych"
