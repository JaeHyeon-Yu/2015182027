from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x, y = 0+25, 90
frame_x, frame_y = 0, 100
move = 5

def Move_Right(x, frame_x, xpos):
    while (x < xpos):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame_x * 100, frame_y, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        x = x + move
        delay(0.01)
        get_events()
def Move_Up(y, frame_x,xpos, ypos):
    x=xpos
    while (y < ypos):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame_x * 100, frame_y, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        y = y + move
        delay(0.01)
        get_events()

def Move_to_Position(xpos, ypos):
       Move_Right(x, frame_x, xpos)
       Move_Up(y, frame_x,xpos, ypos)

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
