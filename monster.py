from abc import ABC, abstractmethod
from pygame import image


class Monster(ABC):

    def __init__(self, pos_x, pos_y, asset):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_image()
        self.asset = image.load(asset)
        self.effective_oil = ''
        self.effective_sword = ''

    @abstractmethod
    def sendImg(self):
        pass

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def get_position(self):
        return self.pos_x, self.pos_y

    @abstractmethod
    def set_image(self):
        pass

    def get_image(self):
        return self.image
