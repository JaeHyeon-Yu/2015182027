from pico2d import *

class Card:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = None
        self.tx, self.ty = 100, 100
        self.sx, self.sy = 120,  100

    def Initialize(self, image, tx, ty):
        self.image = image
        self.tx, self.ty = tx, ty

    def draw(self):
        self.image.draw(self.tx, self.ty)


    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

    def delete(self):
        pass