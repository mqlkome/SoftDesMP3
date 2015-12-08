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
    
    #instantiate the model and view classes
    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)
    controller = PyGameKeyboardController(model)
    
    # it's generally not the best style to declare functions within 
    # and if statement like this
    def rcs_draw(num):
        if event.type==KEYDOWN:                 
            if event.key==K_SPACE:
                ## change the global variable in function
                global showresult_during_keypressed
                showresult_during_keypressed=False
        else:
            view.draw()
            ## show the pick of the computer according to the argument "num"
            show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
            view.show_draw_popup()
            show[num]()

    # all this logic with handling key presses and what they mean
    # both here as well as further down
    # is stuff that I would expect to see in your controller class
    # not so much in the game running file here
    def rcs_win(num):
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE:
                if model.counter <=3:
                    model.change_background()
                    model.change_item()
                    model.change_player_position()
                    model.change_obstacle()
                    global showresult_during_keypressed
                    showresult_during_keypressed=False
                    
                else:
                    #you won the boss battle!
                    pygame.quit()
  
        else:
            if model.counter==4:
                #the princess screen
                view.draw()
                show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
                view.show_win_popup()
                show[num]()
                # this is a really interesting approach
                view.show_final_popup()
            else:
                view.draw()
                show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
                view.show_win_popup()
                show[num]()
                return

    def rcs_lost(num):
        if event.key==pygame.K_a:
            model.reset()
            global showresult_during_keypressed
            showresult_during_keypressed=False
            
            #restart
        else:
            view.draw()
            show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
            view.show_lost_popup()
            show[num]()

    running = True
    while running:
        view.draw()
        if model.player.xposition >= 620:
            if model.counter <= 3:
                model.change_background()
                model.change_obstacle()
                model.change_item()
                model.change_player_position()
            else:
                view.show_final_popup()
                pygame.display.update()
                pygame.time.delay(1000)
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                         if event.key==K_SPACE:
                            pygame.quit() 
                
        #Picking up items:
        if pygame.sprite.collide_rect(model.player, model.item):
            model.player.pick_up_item(model.player, model.item)
            picked_up_item = True
            
        
        if pygame.sprite.collide_rect(model.player, model.item):
            ##Items are solid from the left
            if model.player.previousx <= model.player.xposition:
                if picked_up_item:
                    pass
                else:
                    # you shouldn't have to do controller.model here
                    # you know what the model is, you could just call it by the model variable name
                    # this kind of thing shows you that this code might not be best placed in this file
                    controller.model.player.stepback()        
            ##Items are solid from the right
            elif model.player.previousx >= model.player.xposition:
                if picked_up_item:                  
                    pass
                else:                                        
                    controller.model.player.stepback()

        ##Obstacles are solid from the left
        if pygame.sprite.collide_rect(model.player, model.obstacle): 
            obstcollision = True

            while obstcollision:
                view.show_popup()
                
                if model.player.previousx <= model.player.xposition:
                    controller.model.player.stepback()
                    
                elif model.player.previousx >= model.player.xposition:
                    controller.model.player.stepback()
            
                for event in pygame.event.get():
                    if event.type==KEYDOWN: 
                        obstcollision = False

                        if event.key == K_i:
                            miip = model.item.image_path
                            one = model.obstacle.one
                            two = model.obstacle.two
                            three = model.obstacle.three
                            if miip == one or miip == two or miip == three:
                                view.show_thanks_popup()
                                pygame.display.update()
                                pygame.time.delay(2000)
                                model.obstacle.move()
                                model.item.move()

                        
                            else:
                                view.show_nothanks_popup()
                                pygame.display.update()
                                pygame.time.delay(2000)
                                model.item.move()
                                
                        if event.key==K_f:
                            ##showing the popup for the long time
                            rcnum=randint(0,2)#randomly pick the computer's rock//scissor//paper
                            Time=True
                            # capital-letter variable names should be avoided if possible for convention
                            while Time:
                                for event in pygame.event.get():
                                    if event.type==KEYDOWN:
                                        
                                        ##when player pick rock(pressed R)
                                        if event.key==K_r: 
                                            ##rock image comes out and fight with randomly generated rock scissor paper of computer

                                            showresult_during_keypressed=True
                                            # careful with capital letters on variable names
                                            Oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                if Oneloop:
                                                    view.draw()
                                                    Oneloop=False
                                                view.show_rock()
                                                pygame.time.delay(50)
                                                if rcnum==0:
                                                    for event in pygame.event.get():
                                                        rcs_draw(0)

                                                elif rcnum==1:
                                                    for event in pygame.event.get():
                                                        rcs_win(1)
                                                        
                                                #if computer's pick is paper
                                                elif rcnum==2:
                                                    for event in pygame.event.get():    
                                                        rcs_lost(2)

                                            Time=False
                                            
                                        elif event.key==K_s:
                                            ##scissor image comes out and fight with randomly generated rock scissor paper of computer
                                            showresult_during_keypressed=True
                                            Oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                if Oneloop:
                                                    view.draw()
                                                    Oneloop=False
                                                view.show_scissor()
                                                pygame.time.delay(50)
                                                if rcnum==0:
                                                    for event in pygame.event.get():
                                                        rcs_lost(0)
                                                    
                                                elif rcnum==1:
                                                    for event in pygame.event.get():

                                                        rcs_draw(1)

                                                #if computer's pick is paper
                                                elif rcnum==2:
                                                    for event in pygame.event.get():
                                                        rcs_win(2)
                                            Time=False
                                            
                                        elif event.key==K_p:
                                            showresult_during_keypressed=True
                                            Oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                ##for one time it draws the background to hide the rockscissorpapaer popup
                                                if Oneloop:
                                                    view.draw()
                                                    Oneloop=False
                                                view.show_paper()
                                                pygame.time.delay(50)
                                                if rcnum==0:
                                                    for event in pygame.event.get():
                                                        rcs_win(0)
                                                    
                                                elif rcnum==1:
                                                    for event in pygame.event.get():

                                                        rcs_lost(1)

                                                #if computer's pick is paper
                                                elif rcnum==2:
                                                    for event in pygame.event.get():
                                                        
                                                        rcs_draw(2)
                                            Time=False
                                    else:
                                        view.draw()
                                        view.show_attack()
                                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                controller.handle_key_event(event)

    view.draw()
    
    time.sleep(.050)
    sys.exit()
    pygame.quit()
