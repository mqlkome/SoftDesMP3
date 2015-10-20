# -*- coding: utf-8 -*-
"""
Created on Oct 19, 2015

@author: Jake, Mimi
"""

import pygame
from pygame.locals import *
import os, sys

import model
from model import *
import view
from view import *
import random
from random import randint
import math
import time

            

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen1 = pygame.display.set_mode(size)
    #screen2= pygame.display.set_mode(size)
    background=pygame.image.load("image2.jpg").convert()
    player1=pygame.image.load("images/person1anim.gif")
    player2=pygame.image.load("images/human2.PNG")
    obstacle1=pygame.image.load("images/tree.PNG")
    obstacle2=pygame.image.load("images/bug.png")
    obstacle3=pygame.image.load("images/cat.PNG")
    obstacle4=pygame.image.load("images/princess.png")
    item1=pygame.image.load("images/camera.png")
    item2=pygame.image.load("images/eggplant.png")
    item3=pygame.image.load("images/flower.png")
    item4=pygame.image.load("images/mushroom.png")
    item5=pygame.image.load("images/mysteriousblueorb.png")
    item6=pygame.image.load("images/sword.png")
    sun=pygame.image.load("images/sun.png")
    players=[player1,player2]
    obstacles=[obstacle1,obstacle2,obstacle3,obstacle4]
    items=[item1,item2,item3,item4,item5,item6]

    randplayer=randint(0,1)
    randobstacle=randint(0,2)
    randitem=randint(0,5)
    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)

    # we didn't include the controller yet
    #controller = PyGameMouseController(model)
    #controller = PyGameKeyboardController(model)

    running = True

    while running:
        
        screen1.blit(background,(0,0))
        screen1.blit(players[randplayer],(0,204))
        screen1.blit(obstacles[randobstacle],(550,200))
        screen1.blit(items[randitem],(220,280))
        screen1.blit(sun,(540,20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
#            if event.type == MOUSEMOTION:
#                controller.handle_mouse_event(event)


        view.draw()
        time.sleep(.001)

    pygame.quit()
