# -*- coding: utf-8 -*-
"""
Created on Oct 19, 2015

@author: Jake, Mimi
"""

import pygame
from pygame.locals import *
import os, sys
import PIL as pillow

from model import *
from controller import *
from view import *

from random import randint
import math
import time

#class should be moved to the model


if __name__ == '__main__':
    #initialize pygame
    pygame.init()

    #create a screen of some "size" and load background
    size = (640,480)

    screen1 = pygame.display.set_mode(size)
    background=pygame.image.load("image2.jpg").convert()

   
    #instantiate the model and view classes
    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)
    controller = PyGameKeyboardController(model)

    #controller = PyGameMouseController(model)
    

    running = True
    while running:
        screen1.blit(background,(0,0))
        view.draw()

        #this should happen when you click "pick up item" not automatically when you collide with it
        if pygame.sprite.collide_rect(model.player, model.item):
            model.player.pick_up_item(model.player, model.item)
            picked_up_item = True
        #picked_up_item = False

        #Items are solid from the left
        if pygame.sprite.collide_rect(model.player, model.item):
            if model.player.previousx <= model.player.xposition:
                if picked_up_item:
                    pass
                else:
                    controller.model.player.moveleft()

        #Items are solid from the right        
        if pygame.sprite.collide_rect(model.player, model.obstacle):
            if model.player.previousx >= model.player.xposition:
                if picked_up_item:
                    pass
                else:
                    controller.model.player.moveright()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == KEYDOWN:
                controller.handle_key_event(event)
              
#            if event.type == MOUSEMOTION:
#                controller.handle_mouse_event(event)
        

        view.draw()
        time.sleep(.001)
    sys.exit()
    pygame.quit()
