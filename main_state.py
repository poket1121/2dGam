import random
import json
import os
import sys

from pico2d import *

import game_framework
import title_state
import start_state

from pica import Pica
from map import Map

name = "MainState"

font = None
pica = None
map = None


class Enemy:
    image = None

    def __init__(self):
        self.x, self.y = 300 , 38
        self.frame = random.randint(0,5)
        self.frameSize = 7
        self.dir = -1
        self.life = True

    def update(self):

        Enemy.image = load_image("resource/move_%d.png"%self.frame)
        self.frame = (self.frame+1) % self.frameSize
        self.x += (self.dir * 5)
        if(self.x < 0):
            self.x = 800

        if self.life==False :
            self.x= -10


    def draw(self):
        if self.life ==True:
            self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-40,self.y-40,self.x+40,self.y+40

    def draw_bb(self):
        if self.life ==True:
            draw_rectangle(*self.get_bb())

    def remove(self):
        self.life = False










def handle_events(frame_time):
   events = get_events()
   for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else :
            pica.handle_event(event)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()


    if (right_a > left_b) and (bottom_a < top_b) and (left_a < right_b) :
        if a.Triger == True :
            return 1
        elif a.Triger == False :
            return 2




    return 0







def enter():
    global map,pica,enemy1,dino
    open_canvas(800,400)
    game_framework.reset_time()
    map = Map()
    pica = Pica()
    map.set_center_object(pica)
    pica.set_background(map)
    enemy1 = Enemy()


def exit():
    global map,pica,enemy1,dino
    del(pica)
    del(map)
    del(enemy1)

def pause():
    pass


def resume():
    pass





def update(frame_time):
    pica.update(frame_time)
    map.update(frame_time)
    enemy1.update()
    if collide(pica,enemy1)==1:
        enemy1.remove()
    elif collide(pica,enemy1)==2:
        pica.attacked()


def draw(frame_time):
    clear_canvas()
    map.draw()
    pica.draw()
    pica.draw_life()
    pica.draw_bb()
    enemy1.draw()
    enemy1.draw_bb()
    update_canvas()
    delay(0.05)










