from pico2d import *
import random

open_canvas(1280, 1024)
Ground = load_image('KPU_GROUND.png')
Character = load_image('animation_sheet.png')

size=20
points=[(random.randint(-500,500), random.randint(-350,350)) for i in range(size)]
n=1

x, y=1280//2, 90
frame_x = 0
frame_x = 100

def Move_to_Position(p1, p2):
    pass

while True:
    clear_canvas()
    Ground.draw(1280//2, 1024//2)
    update_canvas()
    Character.clip_draw(frame_x * 100, 100, 100, 100, x, y)
    update_canvas()
    frame_x = (frame_x + 1) % 8
    delay(0.01)
close_canvas()