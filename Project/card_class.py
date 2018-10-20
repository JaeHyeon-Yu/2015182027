from pico2d import *

i = 1

class Card:
    def __init__(self):
        global i
        self.selct = False
        self.useful = True

        if i == 1:
            self.image = load_image('sprites/card/001.png')
        elif i == 2:
            self.image = load_image('sprites/card/002.png')
        elif i == 3:
            self.image = load_image('sprites/card/003.png')
        elif i == 4:
            self.image = load_image('sprites/card/004.png')
        elif i == 5:
            self.image = load_image('sprites/card/005.png')
        elif i == 6:
            self.image = load_image('sprites/card/006.png')
        elif i == 7:
            self.image = load_image('sprites/card/007.png')
        elif i == 8:
            self.image = load_image('sprites/card/008.png')
        elif i == 9:
            self.image = load_image('sprites/card/009.png')
        elif i == 10:
            self.image = load_image('sprites/card/010.png')

    i += 1


