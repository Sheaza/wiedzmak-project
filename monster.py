from abc import ABC, abstractmethod


class Monster(ABC):
    pos_x = None
    pos_y = None
    image = None
    asset = None

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
