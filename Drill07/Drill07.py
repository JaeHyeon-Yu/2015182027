from pico2d import *
import random

open_canvas(1280, 1024)
Ground = load_image('KPU_GROUND.png')
Character = load_image('animation_sheet.png')

size=20
points=[(random.randint(0,1280), random.randint(0,1024)) for i in range(size)]
n=1

x, y=1280//2, 90
frame_x = 0
frame_y = 100



def Move_to_Position(p1, p2):
    global x, y
    global frame_x, frame_y

    if p1[0] > p2[0]:
        frame_y=0
    else:
        frame_y=100


    for i in range(0, 100+1, 2):
        clear_canvas()
        Ground.draw(1280 // 2, 1024 // 2)
        t= i/100
        x=(1-t)*p1[0]+t*p2[0]
        y=(1-t)*p1[1]+t*p2[1]
        Character.clip_draw(frame_x * 100, frame_y, 100, 100, x, y)
        update_canvas()
        frame_x = (frame_x + 1) % 8
        delay(0.01)

while True:
    clear_canvas()
    Ground.draw(1280//2, 1024//2)
    update_canvas()
    Move_to_Position(points[n - 1], points[n])
   # Character.clip_draw(frame_x * 100, frame_y, 100, 100, x, y)
    update_canvas()
    frame_x = (frame_x + 1) % 8
    delay(0.01)
    n = (n + 1) % size
close_canvas()