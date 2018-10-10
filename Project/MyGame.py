from pico2d import *

class Card:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image
class Player:
    def __init__(self):
        self.x, self.y
        self.frame_x, self.frame_y
        self.image=load_image('zeroxsheet.png')
class Monster:
    def __init__(self):
        self.x, self.y
        self.frame_x, self.frame_y

class Background:
    def __init__(self):
        self.image1=load_image('map1.jpg')
        self.image2=load_image('map2.png')
        self.data[6][4]

card=[Card() for i in range(10)]
