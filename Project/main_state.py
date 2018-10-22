from pico2d import *
import game_framework
import title_state
import game_class

name= 'MainState'
hero = game_class.Player()
map = game_class.Background()
image = None

def enter():
    global image
    image = load_image('sprites/stage.png')
    hero.Initialize()
    map.Initialize(load_image('sprites/map1.jpg'))

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    clear_canvas()
    map.draw()
    image.draw(400, 300)
    hero.draw()

    for card in title_state.card_stack:
        card.draw()
    update_canvas()
    delay(0.1)

def update():
    hero.update()

def pause():
    pass

def resume():
    pass