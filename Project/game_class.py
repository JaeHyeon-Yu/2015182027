from pico2d import *
import card_class


class Player:
    def __init__(self):
        self.x, self.y
        self.frame_x, self.frame_y
        self.image= load_image('zeroxsheet.gif')
class Monster:
    def __init__(self):
        self.x, self.y
        self.frame_x, self.frame_y
        self.hp, self.mp
        self.damage

class Background:
    def __init__(self):
        self.image1
        self.image2
        self.data[6][4]
