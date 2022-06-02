from pygame import image
from pygame import transform
import const
from action import Action
from orientation import Orientation
from decision_tree_prediction import DecisionTreePredict
from neural_network_prediction import NeuralNet


class Wiedzmak:
    __instance = None
    __pos_x = None
    __pos_y = None
    __orientation = None
    equipped_sword = None
    equipped_oil = None
    asset = None
    model = None
    neuralNet = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__pos_x, cls.__pos_y = const.START_POS
            cls.__orientation = const.START_ORIENTATION
            cls.asset = image.load('assets\\witcher.png')
            cls.asset = transform.scale(cls.asset, (cls.asset.get_width()*const.scale, cls.asset.get_height()*const.scale))
            cls.model = DecisionTreePredict()
            cls.neuralNet = NeuralNet()
        return super().__new__(cls, *args, **kwargs)

    def move(self, action, monsters, monsters_positions):
        if action == Action.TURN_LEFT:
            if self.__orientation == Orientation.UP: # rotate to the right direction
                self.__orientation = Action.TURN_LEFT.value
                self.asset = image.load(f'assets\\witcher_moveLEFT.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN LEFT")
            elif self.__orientation == Orientation.DOWN: # rotate to the right direction
                self.__orientation = Action.TURN_LEFT.value
                self.asset = image.load(f'assets\\witcher_moveLEFT.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN LEFT")
            elif self.__orientation == Orientation.LEFT: # rotate to the right direction
                self.__orientation = Action.TURN_DOWN.value
                self.asset = image.load(f'assets\\witcher_moveDOWN.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN DOWN")
            elif self.__orientation == Orientation.RIGHT: # rotate to the right direction
                self.__orientation = Action.TURN_UP.value
                self.asset = image.load(f'assets\\witcher_moveUP.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN UP")

        if action == Action.TURN_RIGHT:
            if self.__orientation == Orientation.UP: # rotate to the right direction
                self.__orientation = Action.TURN_RIGHT.value
                self.asset = image.load(f'assets\\witcher_moveRIGHT.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN RIGHT")
            elif self.__orientation == Orientation.DOWN: # rotate to the right direction
                self.__orientation = Action.TURN_RIGHT.value
                self.asset = image.load(f'assets\\witcher_moveRIGHT.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN RIGHT")
            elif self.__orientation == Orientation.LEFT: # rotate to the right direction
                self.__orientation = Action.TURN_UP.value
                self.asset = image.load(f'assets\\witcher_moveUP.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN UP")
            elif self.__orientation == Orientation.RIGHT: # rotate to the right direction
                self.__orientation = Action.TURN_DOWN.value
                self.asset = image.load(f'assets\\witcher_moveDown.png')
                self.asset = transform.scale(self.asset, (self.asset.get_width()*const.scale, self.asset.get_height()*const.scale))
                print(f"DEBUG: TURN DOWN")
        if action == Action.MOVE:
            if self.__orientation == Orientation.UP:
                self.__pos_y += -1
                print(f"DEBUG: MOVE UP")
            elif self.__orientation == Orientation.DOWN:
                self.__pos_y += 1
                print(f"DEBUG: MOVE DOWN")
            elif self.__orientation == Orientation.LEFT:
                self.__pos_x += -1
                print(f"DEBUG: MOVE LEFT")
            elif self.__orientation == Orientation.RIGHT:
                self.__pos_x += 1
                print(f"DEBUG: MOVE RIGHT")
            self.check_for_enemies(self.__pos_x, self.__pos_y, monsters, monsters_positions)
        print(f'("{self.__pos_x},{self.__pos_y},"{self.__orientation}")')   # position after moving

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
        self.equipped_oil = self.neuralNet.predict(target.image) # cnn oil monster class prediction
        self.equipped_sword = self.model.predict(target.attributes) # done decision tree sword prediction

        print(f'FIGHT: witcher uses {self.equipped_sword} and {self.equipped_oil} to defeat {type(target).__name__}...')
        if self.equipped_oil == target.effective_oil and self.equipped_sword == target.effective_sword:
            print('FIGHT: ...and he succeeds!')
            return True
        else:
            print('FIGHT: ...and he fails!')
            return False

    def get_witcher_position(self):
        return self.__pos_x, self.__pos_y

    def get_witcher_orientation(self):
        return self.__orientation
