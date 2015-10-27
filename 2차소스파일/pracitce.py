import random
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
            if event.key == SDLK_ESCAPE:
                running = False

class Pica:
    image = None
    LEFT_RUN,RIGHT_RUN = 0 , 1

    def __init__(self):
        self.x, self.y = 400 , 90
        self.frame = random.randint(0,5)
        self.dir=1
        self.state = self.RIGHT_RUN
        if Pica.image == None:
            Pica.image = load_image('pica.png')


    def update(self):
        if self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1 ) % 5
            self.x += (self.dir * 5 )
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1 ) % 5
            self.x -= (self.dir % 5)

        if self.x>800:
            self.dir = -1
            self.x = 800
            self.state = self.LEFT_RUN
        elif self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.RIGHT_RUN

    def draw(self):
        self.image.clip_draw(self.frame*64,self.state*65,65,65,self.x,self.y)


open_canvas()

pica=Pica()
running = True;

while running:
    handle_events()

    pica.update()
    clear_canvas()
    pica.draw()
    update_canvas()

    delay(0.05)

close_canvas()