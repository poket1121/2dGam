
from pico2d import *

def handle_events():
    global running
    global x
    global direct
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 10
            elif event.key == SDLK_LEFT:
                x = x - 10
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                direct = 0



open_canvas()
character = load_image('pica.png')

running = True
x=0
frame=0
while (x < 800 and running):

    clear_canvas()
    character.clip_draw(frame*64,0,67,62,x,90)
    handle_events()
    update_canvas()
    frame = (frame + 1 ) % 5

    delay(0.05)


close_canvas()