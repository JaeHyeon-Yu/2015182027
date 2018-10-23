from pico2d import *
from card_class import *


class Player:
    def __init__(self):
        self.x, self.y = None, None
        self.frame_x, self.frame_y = None, None
        self.image = None

        self.animation = 1
        self.Idle_animation = [(0, 900), (80, 900)]
        self.run_animation = None
        self.frame = 0
    def Initialize(self):
        self.x, self.y = 120,  410
        self.image = load_image('sprites/zero.png')
    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, 70, 100, self.x, self.y)
    def update(self):
        if self.animation is 1:
            self.frame_x, self.frame_y = self.Idle_animation[self.frame]
            self.frame = (self.frame + 1) % 2
        elif self.animation is 2:
            pass
    def handle_events(self):
        pass

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
