from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def Move_Animation():
    global x, y
    global frame_x
    character.clip_draw(frame_x * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame_x = (frame_x + 1) % 8

def Move_Right(xpos, ypos):
    global x, y
    global frame_x
    ypos +=45
    slope = (ypos - y) / (xpos - x)
    xp, yp = x, y

    while (x <= xpos -40 ):
        y = slope * (x - xp) + yp
        x += 1
        Move_Animation()

def Move_Left(xpos, ypos):
    global x, y
    global frame_x
    slope = (ypos - y) / (xpos - x)
    xp, yp = x, y

    while (x >= xpos):
        y = slope * (x - xp) + yp
        x -= 1
        Move_Animation()

def Move_to_Position(xpos, ypos):
    global x, y
    global running
    running= True
    if (xpos > x) :
        Move_Right(xpos, ypos)
    else:
        Move_Left(xpos, ypos)

def handle_events():
    global running
    global mouse_x, mouse_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT -1 -event.y
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running=False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            Move_to_Position(event.x, KPU_HEIGHT -1 -event.y)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = False
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame_x = 0
hide_cursor()

while True:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0, 0, 100, 100, mouse_x, mouse_y)
    Move_Animation()
    update_canvas()
    if(running== False):
        delay(0.05)
    handle_events()

close_canvas()




