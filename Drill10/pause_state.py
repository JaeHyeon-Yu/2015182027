import game_framework
from pico2d import *
import main_state

name= "PauseState"
image= None
pause_dir = True
count=0

def enter():
    global image
    image=load_image('pause.png')

def exit():
    global image
    del(image)

def draw():
    global image, count
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    #update_canvas()
    if count%2==0:
        image.clip_draw(200, 200, 500, 500, 400, 350)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    global count
    count += 1
    delay(0.2)

def pause():
    pass


def resume():
    pass