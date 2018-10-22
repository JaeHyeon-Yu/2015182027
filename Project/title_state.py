from pico2d import *
import game_framework
import main_state
import game_class

name= "TitleState"
image= None
card_stack = 0  # 턴 시작전 사용할 카드 선정!

#card001=game_class.card_class.Card001()
deck=[game_class.card_class.Card() for i in range(10)]


def enter():
    global image
    image = load_image('sprites/cardselect.png')
    
    deck[0] = load_image('sprites/card/001.png')
    deck[1] = load_image('sprites/card/002.png')
    deck[2] = load_image('sprites/card/003.png')
    deck[3] = load_image('sprites/card/004.png')
    deck[4] = load_image('sprites/card/005.png')
    deck[5] = load_image('sprites/card/006.png')
    deck[6] = load_image('sprites/card/007.png')
    deck[7] = load_image('sprites/card/008.png')
    deck[8] = load_image('sprites/card/009.png')
    deck[9] = load_image('sprites/card/010.png')


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