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

if __name__ == '__main__':
    #initialize pygame
    pygame.init()

    #create a screen of some "size" and load background
    size = (640,480)
    screen1 = pygame.display.set_mode(size)
    background1=pygame.image.load("images/bluesky.png").convert()
    background2=pygame.image.load("images/mountain.png").convert()
    background3=pygame.image.load("images/fire.png").convert()
    background4=pygame.image.load("images/castle.png").convert()

    #rsplist=[view.rock_obs,view.scissor_obs,view.paper_obs]
    #instantiate the model and view classes

    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)
    controller = PyGameKeyboardController(model)
   

    running = True
    while running:
        screen1.blit(background1,(0,0))
        view.draw()

        #Picking up items: this should happen when you press the key for "pick up item" not automatically when you collide with it:
        if pygame.sprite.collide_rect(model.player, model.item):
            model.player.pick_up_item(model.player, model.item)
            picked_up_item = True
        #picked_up_item = False

        ##Items are solid from the left
        if pygame.sprite.collide_rect(model.player, model.item):
            if model.player.previousx <= model.player.xposition:
                if picked_up_item:
                    pass
                else:
                    controller.model.player.moveleft()
        ##Items are solid from the right
            elif model.player.previousx >= model.player.xposition:
                if picked_up_item:                  
                    pass
                else:                                        
                    controller.model.player.moveright()

        ##Obstacles are solid from the left
        ##THIS WILL BE MODIFIED SO THAT A SUCCESFUL BRIBE OR WIN IN A FIGHT WILL ALLOW YOU TO PASS
        if pygame.sprite.collide_rect(model.player, model.obstacle):
            if model.player.previousx <= model.player.xposition:
                controller.model.player.moveleft()
            elif model.player.previousx >= model.player.xposition:
                controller.model.player.moveright()


            
            if event.type==KEYDOWN: 
                if event.key==K_f:
                    ##showing the popup for the long time
                    rcnum=randint(0,2)#randomly pick the computer's rock//scissor//paper
                    Time=True
                    while Time:
                        for event in pygame.event.get():
                            if event.type==KEYDOWN:
                                
                                ##when player pick rock(pressed R)
                                if event.key==K_r: 
                                    """rock image comes out and fight with randomly generated rock scissor paper of computer"""

                                    """how can I change the pop up?
                                    not showing the whold rsp and just showing rock picture"""
                                    
                                    # view.show_rock()
                                    # pygame.time.delay(1000)
                                    showresult_during_keypressed=True
                                    while showresult_during_keypressed:
                                        view.show_rock()
                                        pygame.time.delay(50)
                                        if rcnum==0:
                                            #rclist[rcnum]
                                            #print "draw" #change this with graphics later on
                                            for event in pygame.event.get():
                                                
                                                if event.key==K_SPACE:
                                                    showresult_during_keypressed=False
                                                else:
                                                    print "draw"
                                                    view.show_rock_obs()
                                                    
                                                    #view.show_draw
                                                    




                                        elif rcnum==1:
                                            for event in pygame.event.get():

                                                if event.key==pygame.K_SPACE:
                                                    background1=background2
                                                    model.change_obstacle()
                                                    model.change_item()
                                                    model.change_player_position()

                                                    showresult_during_keypressed=False
                                                    #change item. change obstacle
                                                    #change player position
                                                else:
                                                    print "player win"
                                                    print "press SPACE to go to second round"
                                                    view.show_scissor_obs()


                                        #if computer's pick is paper
                                        elif rcnum==2:
                                            for event_new in pygame.event.get():
                                                
                                                if event_new.key==pygame.K_a:
                                                    
                                                    showresult_during_keypressed=False
                                                    pygame.quit()
                                                    #restart
                                                else:
                                                    print "player lost" #change it to graphics
                                                    view.show_paper_obs()
                                                    # choosing_playagain=True
                                                    # while choosing_playagain:
                                                    
                                                        
                                                    #     if event.key==pygame.K_a:
                                                    #         choosing_playagain=False
                                                    #         pygame.init()
                                                    #     else:
                                                    #         view.show_scissor_obs()
                                                    #         print "not getting a yet"#for checking needto change with press a to play again


                                                    #show gameover sign, play again sign

                                    Time=False
                                    
                                    #rclist[rcnum]
                                elif event.key==K_s:
                                    Time=False
                                    view.show_scissor
                                elif event.key==K_p:
                                    Time=False
                                    view.show_paper
                            else:
                                view.show_attack()
                                print "show attack"

                        


                    
            else:
                view.show_popup()

            
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                controller.handle_key_event(event)

#            if event.type == MOUSEMOTION:
#                controller.handle_mouse_event(event)

    view.draw()
    
    time.sleep(.050)
    sys.exit()
    pygame.quit()
