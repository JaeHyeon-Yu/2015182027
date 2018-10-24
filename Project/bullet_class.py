from pico2d import *

class Bullet:
    def __init__(self):
        self.x, self.y = None, None
        self.image = None

    def Initialize(self, x, y):
        self.x, self.y = x + 50, y
        self.image = load_image('sprites/bullet.png')

    def update(self):
        self.x += 10

    def draw(self):
        self.image.draw(self.x , self.y)