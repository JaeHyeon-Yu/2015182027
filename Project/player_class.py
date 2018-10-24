from pico2d import *
import game_framework
from bullet_class import *


class Player:
    def __init__(self):
        self.x, self.y = None, None
        self.frame_x, self.frame_y = None, None
        self.size_x, self.size_y = 80, 100
        self.image = None

        self.gun = False
        self.bullet = Bullet()

        self.animation = 4
        self.Idle_animation = [(0, 900), (75, 900)]   # 1
        self.run_animation = [(0, 500), (80, 500), (160, 500), (240, 500), (320, 500), (400, 500), (480, 500), (570, 500), (650, 500), (740, 500), (820, 500), (895, 500), (975, 500), (1055, 500), (1135, 500), (1220, 500)]    # 2
        self.jump_animation = [(0, 760), (70, 745), (137, 740)]  # 3    # 나중에 찾자.....
        self.gun_animation = [(0, 630), (75, 630), (155, 630), (240, 630), (325, 630), (408, 630), (492, 630), (600, 630), (325, 630), (240, 630), (155, 630)]  # 4
        self.attack_animation = [(0, 420), (90, 420), (182, 420), (265, 420), (440, 420), (605, 420), (760, 420), (880, 420), (1000, 420), (90, 420)] #5
        self.frame = 0
    def Initialize(self):
        self.x, self.y = 120,  410
        self.image = load_image('sprites/zerox.png')

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)
        if self.gun is True:
            self.bullet.draw()

    def update(self):
        if self.animation is 1:
            self.size_x = 75
            self.frame_x, self.frame_y = self.Idle_animation[self.frame]
            self.frame = (self.frame + 1) % 2
        elif self.animation is 2:
            self.frame_x, self.frame_y = self.run_animation[self.frame]
            self.frame = (self.frame + 1) % 16
            self.x += 200//16
            if self.frame is 15:
                self.x=300
                self.frame = 0
                self.animation = 1
        elif self.animation is 3:
            pass
        elif self.animation is 4:
            if self.frame is 5:
                self.size_x = 88
            elif self.frame is 6:
                self.size_x = 100
            elif self.frame is 7:
                self.size_x = 120
            else:
                self.size_x = 80
            self.frame_x, self.frame_y = self.gun_animation[self.frame]
            self.frame = (self.frame +1) % 11
        elif self.animation is 5:
            if self.frame is 3 or self.frame is 4:
                self.size_x = 160
            elif self.frame is 5:
                self.size_x = 140
            elif self.frame is 6 or self.frame is 7:
                self.size_x = 105
            elif self.frame is 9:
                self.gun = True
                self.bullet.Initialize(self.x, self.y)
            else:
                self.size_x = 80
            self.frame_x, self.frame_y = self.attack_animation[self.frame]
            self.frame = (self.frame+1)% 10

            if self.frame is 9:
                self.frame = 0
                self.animation = 1

    def handle_events(self):
        pass