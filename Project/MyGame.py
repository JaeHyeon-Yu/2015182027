from pico2d import *
import game_framework
import title_state

class Card:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image
class Player:
    def __init__(self):
        self.x, self.y
        self.frame_x, self.frame_y
        self.image
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


open_canvas()