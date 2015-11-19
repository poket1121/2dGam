import random
import json
import os
import sys

from pico2d import *

import game_framework
import title_state
import start_state


name = "MainState"

grass = None
font = None


class map:
    def __init__(self):
        self.image = load_image('map.png')

    def draw(self):
        self.image.draw(100, 300)

class Enemy:
    image = None

    def __init__(self):
        self.x, self.y = 300 , 38
        self.frame = random.randint(0,5)
        self.frameSize = 7
        self.dir = -1

    def update(self):

        Enemy.image = load_image("resource/move_%d.png"%self.frame)
        self.frame = (self.frame+1) % self.frameSize
        self.x += (self.dir * 5)
        if(self.x < 0):
            self.x = 600


    def draw(self):
        self.image.draw(self.x,self.y)



class Pica:
    image = None
    LEFT_RUN,RIGHT_RUN = 0 , 1
    LEFT_STAND,RIGHT_STAND = 2, 3
    JUMP = 4

    PIXEL_PER_METER = (10.0 /0.3) #   10 pixel 30cm
    RUN_SPEED_KMPH = 20.0        # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8



    def __init__(self):
        self.x, self.y = 400 , 30
        self.frame = random.randint(0,5)
        self.state = self.RIGHT_RUN
        self.JUMP = 0
        if Pica.image == None:
            Pica.image = load_image('pica.png')

    def handle_event(self,event):
        if (event.type, event.key) == (SDL_KEYDOWN,SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
            elif self.state == self.RIGHT_RUN:
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND,self.LEFT_STAND):
                self.state = self.RIGHT_RUN
            elif self.state == self.LEFT_RUN:
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type,event.key) == (SDL_KEYUP,SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND


        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
           if(self.JUMP == 0):
               self.JUMP = 1
    
    def pica_bb(self):
        pass

    def update(self):

        if self.JUMP == 1:
            self.y += 10
            if(self.y >= 50):
                self.JUMP = 2
        elif self.JUMP == 2:
            self.y += 5
            if(self.y >= 80):
                self.JUMP = 3
        elif self.JUMP == 3:
            self.y -= 5
            if(self.y <= 50):
                self.JUMP = 4
        elif self.JUMP == 4:
            self.y -= 10
            if(self.y <= 30):
                self.JUMP = 0
        elif self.JUMP == 0:
            pass

        if self.state == self.RIGHT_RUN:
            self.frame = int(self.frame + 1)%5
            self.x += 5
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 1 ) % 5
            self.x -=5
        elif self.state == self.RIGHT_STAND:
            pass
        elif self.state == self.LEFT_STAND:
            pass


    def draw(self):
        self.image.clip_draw(self.frame*64,self.state*65,65,65,self.x,self.y)



def handle_events():
   events = get_events()
   for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else :
            pica.handle_event(event)

def enter():
    global map,pica,enemy1
    map = map()
    pica = Pica()
    enemy1 = Enemy()

def exit():
    global map,pica,enemy1
    del(pica)
    del(map)
    del(enemy1)

def pause():
    pass


def resume():
    pass





def update():
    pica.update()
    enemy1.update()

def draw():
    clear_canvas()
    map.draw()
    pica.draw()
    enemy1.draw()
    update_canvas()
    delay(0.05)










