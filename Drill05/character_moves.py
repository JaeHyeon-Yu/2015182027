from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x, y=0+25, 90

def Move_Right():
    pass

def Move_Left():
    pass


def Move_to_Position(xpos, ypos):
     if (x < xpos):
         Move_Right()
     else :
         Move_Left()

while True:
    Move_to_Position(203, 535)
    Move_to_Position(132, 243)
    Move_to_Position(535, 470)
    Move_to_Position(477, 203)
    Move_to_Position(715, 136)
    Move_to_Position(316, 225)
    Move_to_Position(510, 92)
    Move_to_Position(692, 518)
    Move_to_Position(682, 336)
    Move_to_Position(712, 349)


close_canvas()
