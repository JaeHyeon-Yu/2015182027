from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')
character = load_image('animation_sheet.png')

x=0
frame=0
frame_y=100
move=5
while(True):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100, frame_y, 100, 100, x, 90)
    update_canvas()
    frame=(frame+1)%8
    x=x+move

    delay(0.02)
    get_events()

    if(x>800-15):
        frame_y= 0
        move= -5
    elif(x<0+15):
        frame_y= 100
        move= 5

close_canvas()
