from pico2d import *

class Card:
    def __init__(self):
        self.image = None
        self.tx, self.ty = 0, 0
        self.sx, self.sy = 0,  0

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

    def Check(self):
        if self.image == None:
            return True
        else:
            return False

    def delete(self):
        self.image = None
        pass