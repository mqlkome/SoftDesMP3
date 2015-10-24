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
import controller
from controller import*
import random
from random import randint
import math
import time

            


if __name__ == '__main__':
    pygame.init()

    size = (640,480)

    #loading the images we made
    screen1 = pygame.display.set_mode(size)
    #screen2= pygame.display.set_mode(size)
    background=pygame.image.load("image2.jpg").convert()
    background2=pygame.image.load("image3.jpg").convert()
    # player1=pygame.image.load("images/human1.png")
    # player2=pygame.image.load("images/human2.PNG")
    # #player's default position

    # player_pos_x=0
    # player_pos_y=204

    # obstacle1=pygame.image.load("images/tree.PNG")
    # obstacle2=pygame.image.load("images/bug.png")
    # obstacle3=pygame.image.load("images/cat.PNG")
    # obstacle4=pygame.image.load("images/princess.png")
    # item1=pygame.image.load("images/camera.png")
    # item2=pygame.image.load("images/eggplant.png")
    # item3=pygame.image.load("images/flower.png")
    # item4=pygame.image.load("images/mushroom.png")
    # item5=pygame.image.load("images/mysteriousblueorb.png")
    # item6=pygame.image.load("images/sword.png")
    #sun=pygame.image.load("images/sun.png")
    #players=[player1,player2]
    # obstacles=[obstacle1,obstacle2,obstacle3,obstacle4]
    # items=[item1,item2,item3,item4,item5,item6]

    #choosing the random images
    num_player=[0,1]
    num_obstacle=[0,1,2]
    num_item=[0,1,2,3,4,5]

    randplayer=randint(0,1)
    randobstacle=randint(0,2)
    randitem=randint(0,5)
    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)

    # we didn't include the controller yet
    #controller = PyGameMouseController(model)
    controller = PyGameKeyboardController(model)

    running = True
    
    while running:

        screen1.blit(background,(0,0))
        #screen1.blit(players[randplayer],player_pos)
        #screen1.blit(obstacles[randobstacle],(550,200))
        #screen1.blit(items[randitem],(220,280))
        #screen1.blit(sun,(540,20))

        model.player.assign_int=randplayer
        model.obstacle.assign_int=randobstacle
        model.item.assign_int=randitem

        view.show_popup()

        view.draw()
        #view.make_popup()
        time.sleep(.001)
        
        

        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                controller.handle_key_event(event)
                
         #change to the second screen

        if model.player.x>=630:
            background=background2
            model.player.x=0 
            model.sun.x+= -60
            model.sun.y+= 2 

            ##exclde the numbers from the list for the next random number
            # making new random obstacle
            num_obstacle.pop(randobstacle)
            randobstacle=num_obstacle[randint(0,len(num_obstacle)-1)]
            model.obstacle.assign_int=randobstacle
            
            ##making new random obstacle
            #model.item.assign_int=
            view.show_popup()





                    

                 

    pygame.quit()
