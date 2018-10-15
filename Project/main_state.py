from pico2d import *
import game_framework
import title_state
import game_class

name= 'MainState'

def enter():
    pass

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    pass

def update():
    pass

def pause():
    pass

def resume():
    pass