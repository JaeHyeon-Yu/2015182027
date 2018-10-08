from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x +=5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(500, 600)
        self.size=random.randint(1,2)
        if self.size == 1:
            self.image=load_image('ball21x21.png')
        else:
            self.image=load_image('ball41x24')

    def update(self):
        self.y -= 5

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team=[Boy() for i in range(11)]
grass = Grass()
balls = [Ball() for i in range(20)]

running = True