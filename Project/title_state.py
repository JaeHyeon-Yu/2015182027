from pico2d import *
import game_framework
import main_state
import game_class

name= "TitleState"
image= None
card_stack = None  # 턴 시작전 사용할 카드 선정!

deck = [None for i in range(10)]


def enter():
    global image
    global deck
    image = load_image('sprites/cardselect.png')

    deck[0] = game_class.Card001()
    deck[1] = game_class.Card002()
    deck[2] = game_class.Card003()
    deck[3] = game_class.Card004()
    deck[4] = game_class.Card005()
    deck[5] = game_class.Card006()
    deck[6] = game_class.Card007()
    deck[7] = game_class.Card008()
    deck[8] = game_class.Card009()
    deck[9] = game_class.Card010()



def exit():
    global image
    del (image)

def handle_events():
    global stack
    global deck

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.type == SDL_MOUSEBUTTONDOWN:
                x, y = event.x, 600-1-event.y

                i = 0
                while i<10 :
                    if deck[0].Click(x, y):
                        pass
                    i += 1





def draw():
    global image
    global stack
    global deck


    clear_canvas()
    image.draw(400, 300)

    i=0
    while i<10:
        deck[i].draw()
        i += 1

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass