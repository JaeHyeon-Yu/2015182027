from pico2d import *

class Card001:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/001.png')
        self.tx, self.ty = 170, 500

    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card002:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/002.png')
        self.tx, self.ty = 170 +114, 500
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card003:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/003.png')
        self.tx, self.ty = 170 + 114*2, 500
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card004:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/004.png')
        self.tx, self.ty = 170 + 114*3, 500
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card005:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/005.png')
        self.tx, self.ty = 170 + 114*4, 500
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card006:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/006.png')
        self.tx, self.ty = 170 , 300
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card007:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/007.png')
        self.tx, self.ty = 170 + 114, 300
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card008:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/008.png')
        self.tx, self.ty = 170 + 114 * 2, 300
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False


class Card009:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/009.png')
        self.tx, self.ty = 170 + 114 * 3, 300
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False

class Card010:
    def __init__(self):
        self.selct = False
        self.useful = True
        self.image = load_image('sprites/card/010.png')
        self.tx, self.ty = 170 + 114 * 4, 300
    def draw(self):
        self.image.draw(self.tx, self.ty)

    def Click(self, x, y):
        if self.tx - 57 <= x and x <= self.tx + 57 and self.ty - 73 <= y and y <= self.ty + 73:
            return True
        else:
            return False