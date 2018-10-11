import game_framework
from pico2d import *
import main_state

name= "PauseState"
image= None
pause_dir = True

def enter():
    global image
    image=load_image('pause.png')

def exit():
    global image
    del(image)

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    pass


def pause():
    pass


def resume():
    pass