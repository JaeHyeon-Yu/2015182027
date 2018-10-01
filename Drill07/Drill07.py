from pico2d import *
import random

open_canvas(1280, 1024)
Ground = load_image('KPU_GROUND.png')
Character = load_image('animation_sheet.png')



while True:
    clear_canvas()
    Ground.draw(1280//2, 1024//2)
    update_canvas()

close_canvas()