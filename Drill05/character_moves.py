from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x, y=0+25, 90
frame_x = 0

def Move_Animation(frame_y) :
    global x, y, frame_x
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_x * 100, frame_y, 100, 100, x, y)
    update_canvas()
    frame_x = (frame_x + 1) % 8
    delay(0.02)
    get_events()

def Move_Right(xpos, ypos):
    global x, y, frame_x
    slope = (ypos-y)/(xpos-x)
    xp, yp = x, y
    while (x <= xpos):
        Move_Animation(100)
        y = slope * (x-xp) + yp
        x+=1

def Move_Left(xpos, ypos):
    global x, y, frame_x
    slope = (ypos - y) / (xpos - x)
    xp, yp = x, y
    while (x >= xpos):
        Move_Animation(200)
        y = slope * (x - xp) + yp
        x -= 1

def Move_to_Position(xpos, ypos):
    global x, y
    if (x < xpos):
        Move_Right(xpos, ypos)
    elif (x > xpos) :
        Move_Left(xpos, ypos)

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
