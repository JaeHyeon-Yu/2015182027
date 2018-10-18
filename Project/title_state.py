from pico2d import *
import game_framework
import main_state
import game_class

name= "TitleState"
image= None


def enter():
    global image
    image = load_image('sprites/cardselect.png')

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass