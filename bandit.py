from monster import Monster
from oils import Oil
from swords import Sword


class Bandit(Monster):
    counter = 0

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, 'assets\\bandyta.png')
        self.image = 'training/bandit/20220529075556_1.jpg'
        self.effective_oil = Oil.KUJAWSKI
        self.effective_sword = Sword.STEEL
        self.attributes = [0,0,0,0,1,0,0,3] #'pazury', 'skrzydla', 'ogon', 'siersc', 'dwie nogi', 'kly', 'rogi', 'humanoidalnosc'

        Bandit.counter += 1
        print("spawned bandit", Bandit.counter)

    def get_position(self):
        return super().get_position()

    def sendImg(self):
        print("bandyta")

    def set_image(self):
        self.image = "zdjecie z setu danych"
