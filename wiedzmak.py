from pygame import image
from pygame import transform
import const


class Wiedzmak:
    __instance = None
    __pos_x = None
    __pos_y = None
    __orientation = None
    equipped_sword = None
    equipped_oil = None
    asset = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__pos_x, cls.__pos_y, cls.__orientation = const.START_POS
            cls.asset = image.load('assets\\witcher.png')
            cls.asset = transform.scale(cls.asset, (cls.asset.get_width()*const.scale, cls.asset.get_height()*const.scale))
        return super().__new__(cls, *args, **kwargs)

    def move(self, direction, monsters, monsters_positions):
        if direction == 'LEFT':
            if self.__orientation == direction: # if orientated in right direction then try to go in that direction
                if self.__pos_x - 1 > -1 and (self.__pos_x - 1, self.__pos_y) not in const.COLLISIONS:
                    self.check_for_enemies(self.__pos_x-1,self.__pos_y, monsters, monsters_positions)
                    self.__pos_x -= 1
            else:   # rotate to the right direction
                self.__orientation = direction
                self.asset = image.load(f'assets\\witcher_move{direction}.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN {direction}")

        elif direction == 'RIGHT':
            if self.__orientation == direction: # if orientated in right direction then try to go in that direction
                if self.__pos_x + 1 < 48 and (self.__pos_x + 1, self.__pos_y) not in const.COLLISIONS:
                    self.check_for_enemies(self.__pos_x + 1, self.__pos_y, monsters, monsters_positions)
                    self.__pos_x += 1
            else:   # rotate to the right direction
                self.__orientation = direction
                self.asset = image.load(f'assets\\witcher_move{direction}.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN {direction}")

        elif direction == 'UP':
            if self.__orientation == direction: # if orientated in right direction then try to go in that direction
                if self.__pos_y - 1 > -1 and (self.__pos_x, self.__pos_y - 1) not in const.COLLISIONS:
                    self.check_for_enemies(self.__pos_x, self.__pos_y - 1, monsters, monsters_positions)
                    self.__pos_y -= 1
            else:   # rotate to the right direction
                self.__orientation = direction
                self.asset = image.load(f'assets\\witcher_move{direction}.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN {direction}")

        elif direction == 'DOWN':
            if self.__orientation == direction: # if orientated in right direction then try to go in that direction
                if self.__pos_y + 1 < 48 and (self.__pos_x, self.__pos_y + 1) not in const.COLLISIONS:
                    self.check_for_enemies(self.__pos_x, self.__pos_y + 1, monsters, monsters_positions)
                    self.__pos_y += 1
            else:   # rotate to the right direction
                self.__orientation = direction
                self.asset = image.load(f'assets\\witcher_move{direction}.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN {direction}")
        
        print(f'("{self.__pos_x},{self.__pos_y},"{self.__orientation}")')   # position after moving
        #seq.append((self.__pos_x,self.__pos_y,self.__orientation))         # TODO data for seq !!!!

    def check_for_enemies(self, checkX, checkY, monsters, monsters_positions):
        if (checkX,checkY) in monsters_positions:                           # checking given position for monsters
                    print("--- fight! ---")
                    for x in monsters:                                      # picking encountered monster from the list
                        if (x.pos_x,x.pos_y) == (checkX,checkY):
                            if self.fight(x):                               # fight and results
                                monsters.remove(x)
                                monsters_positions.remove((checkX,checkY))
                            else:
                                print('witcher_dead')
                    print('other monsters: ',monsters_positions)
                    print('--------')

    def fight(self, target):    # fight mechanics
        # TODO: monster recognition and equipment selection mechanics
        self.equipped_oil = target.effective_oil
        self.equipped_sword = target.effective_sword

        print(f'FIGHT: witcher uses {self.equipped_sword} and {self.equipped_oil} to defeat {type(target).__name__}...')
        if self.equipped_oil == target.effective_oil and self.equipped_sword == target.effective_sword:
            print('FIGHT: ...and he succeeds!')
            return True
        else:
            print('FIGHT: ...and he fails!')
            return False


    def get_witcher_position(self):
        return self.__pos_x, self.__pos_y
