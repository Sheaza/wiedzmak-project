from pygame import image
from pygame import transform
import const


class Wiedzmak:
    __instance = None
    __pos_x = None
    __pos_y = None
    asset = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__pos_x, cls.__pos_y = const.START_POS
            cls.asset = image.load('assets\\witcher.png')
            cls.asset = transform.scale(cls.asset, (cls.asset.get_width()*const.scale, cls.asset.get_height()*const.scale))
        return super().__new__(cls, *args, **kwargs)

    def move(self, direction):
        if direction == 'LEFT' and self.__pos_x - 1 > -1 and (self.__pos_x - 1, self.__pos_y) not in const.COLLISIONS:
            self.__pos_x -= 1
        elif direction == 'RIGHT' and self.__pos_x + 1 < 48 and (self.__pos_x + 1, self.__pos_y) not in const.COLLISIONS:
            self.__pos_x += 1
        elif direction == 'UP' and self.__pos_y - 1 > -1 and (self.__pos_x, self.__pos_y - 1) not in const.COLLISIONS:
            self.__pos_y -= 1
        elif direction == 'DOWN' and self.__pos_y + 1 < 48 and (self.__pos_x, self.__pos_y + 1) not in const.COLLISIONS:
            self.__pos_y += 1

    def get_witcher_position(self):
        return self.__pos_x, self.__pos_y


