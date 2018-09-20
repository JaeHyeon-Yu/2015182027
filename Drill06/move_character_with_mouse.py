from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mouse_x, mouse_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT -1 -event.y
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running=False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame_x = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0, 0, 100, 100, mouse_x, mouse_y)
    character.clip_draw(frame_x * 100, 100 * 1, 100, 100, x, 90)
    update_canvas()
    frame_x = (frame_x + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()




