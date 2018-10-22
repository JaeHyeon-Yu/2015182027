from pico2d import *
import game_framework
import start_state
import game_class

name= 'MainState'
#hero = game_class.Player()
image = None

def enter():
    global image
    image = load_image('sprites/map1.jpg')

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass