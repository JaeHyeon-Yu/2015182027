from pico2d import *
import game_framework
import main_state
import game_class

name= "TitleState"
image= None
card_stack = 0  # 턴 시작전 사용할 카드 선정!

cards = [game_class.card_class.Card() for card in range(10)]




def enter():
    global image
    image = load_image('sprites/cardselect.png')

def exit():
    global image
    del (image)

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