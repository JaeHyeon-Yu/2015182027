from pico2d import *
from card_class import *


class Player:
    def __init__(self):
        self.x, self.y = None, None
        self.frame_x, self.frame_y = None, None
        self.image = None
    def Initialize(self):
        self.x, self.y = 100,  400
        self.image = load_image('sprites/zeroxsheet.gif')
        self.frame_x, self.frame_y = 0, 350
    def draw(self):
        self.image.clip_draw((self.frame_x*54), self.frame_y, 54, 50, self.x, self.y)
    def update(self):
        self.frame_x = (self.frame_x+1) % 16


class Monster:
    def __init__(self):
        self.x, self.y
        self.frame_x, self.frame_y
        self.hp, self.mp
        self.damage

class Background:
    def __init__(self):
        self.image = None
    def Initialize(self, image):
        self.image = image

    def draw(self):
        self.image.draw(400, 300)
