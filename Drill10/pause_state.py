import game_framework
from pico2d import *

name= "PauseState"
image= None

def enter():
    global image
    image=load_image('pause.png')