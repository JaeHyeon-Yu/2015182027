from pico2d import *
import game_framework
import main_state

name= "TitleState"
image= None

def enter():
    image=load_image('title(beta).png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
                game_framework.quit()

def draw():
    pass

def update():
    pass

def pause():
    pass

def resume():
    pass