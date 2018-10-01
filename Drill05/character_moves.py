from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

x, y = 0+25, 90
frame_x = 0

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def Move_Animation(frame_y) :
    global x, y, frame_x
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_x * 100, frame_y, 100, 100, x, y)
    update_canvas()
    frame_x = (frame_x + 1) % 8
    delay(0.01)
    get_events()

def Move_Right(xpos, ypos):
    global x, y
    slope = (ypos-y)/(xpos-x)
    xp, yp = x, y

    while (x <= xpos):
        Move_Animation(100)
        y = slope * (x - xp) + yp
        x += 1

def Move_Left(xpos, ypos):
    global x, y
    slope = (ypos - y) / (xpos - x)
    xp, yp = x, y

    while (x >= xpos):
        Move_Animation(0)
        y = slope * (x - xp) + yp
        x -= 1

def Move_to_Position(xpos, ypos):
    global x, y
    if (x < xpos):
        Move_Right(xpos, ypos)
    elif (x > xpos) :
        Move_Left(xpos, ypos)

while True:
    #Move_to_Position(203, 535)
   # Move_to_Position(132, 243)
    #Move_to_Position(535, 470)
    #Move_to_Position(477, 203)
    #Move_to_Position(715, 136)
    #Move_to_Position(316, 225)
    #Move_to_Position(510, 92)
    #Move_to_Position(692, 518)
    #Move_to_Position(682, 336)
    #Move_to_Position(712, 349)

close_canvas()
