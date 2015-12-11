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
# all this logic with handling key presses and what they mean
# both here as well as further down
# is stuff that I would expect to see in your controller class
# not so much in the game running file here


# result of RockPaperScissors is a draw
def rcs_draw(num):
    if event.type==KEYDOWN:                 
        if event.key==K_SPACE:
            ## change the global variable in function
            global showresult_during_keypressed
            showresult_during_keypressed=False
    else:
        view.draw()
        ## show the pick of the computer according to the argument "num"
        obs_choices = [model.rock_obs, model.scissor_obs, model.paper_obs]
        view.show(obs_choices[num])
        view.show_popup("images/draw_popup.jpg")
        
#result of RockPaperScissors is player wins
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
            obs_choices = [model.rock_obs, model.scissor_obs, model.paper_obs]
            view.show(obs_choices[num])
            view.show_popup("images/win_popup.jpg")
            view.show_popup("images/final_popup.jpg")
        else:
            view.draw()
            obs_choices = [model.rock_obs, model.scissor_obs, model.paper_obs]
            view.show(obs_choices[num])
            view.show_popup("images/win_popup.jpg")
            return

#result of RockPaperScissors is player loses
def rcs_lost(num):
    if event.key==pygame.K_a:
        model.reset()
        global showresult_during_keypressed
        showresult_during_keypressed=False
        
        #restart
    else:
        view.draw()
        obs_choices = [model.rock_obs, model.scissor_obs, model.paper_obs]
        view.show(obs_choices[num])
        view.show_popup("images/lost_popup.jpg")


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
    
    running = True
    while running:
        #load the next screen when you get to the right edge:
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
                    controller.handle_key_event(event)
                    
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
                    model.player.stepback()        
            ##Items are solid from the right
            elif model.player.previousx >= model.player.xposition:
                if picked_up_item:                  
                    pass
                else:                                        
                    controller.model.player.stepback()

        if pygame.sprite.collide_rect(model.player, model.obstacle): 
            obstcollision = True
            while obstcollision:
                view.show(model.popup)
                #obstacle is solid from both sides
                if model.player.previousx <= model.player.xposition:
                    controller.model.player.stepback()
                elif model.player.previousx >= model.player.xposition:
                    controller.model.player.stepback()
            
                for event in pygame.event.get():
                    if event.type==KEYDOWN: 
                        obstcollision = False

                        if event.key == K_i:  ##you've offered the item
                            miip = model.item.image_path
                            one = model.obstacle.one
                            two = model.obstacle.two
                            three = model.obstacle.three
                            if miip == one or miip == two or miip == three:  #it wants the item
                                view.show_speech("images/thanks_popup.png")
                                pygame.display.update()
                                pygame.time.delay(2000)
                                model.obstacle.move()
                                model.item.move()
                        
                            else: ##it doesn't want the item
                                view.show_speech("images/nothanks_popup.png")
                                pygame.display.update()
                                pygame.time.delay(2000)
                                model.item.move()
                                
                        if event.key==K_f: ##you've chosen to fight
                            rcnum=randint(0,2)#randomly pick the computer's rock//scissor//paper
                            time=True
                            while time:
                                for event in pygame.event.get():
                                    if event.type==KEYDOWN:
                                        
                                        ##when player pick rock(pressed R)
                                        if event.key==K_r: ##player chose rock
                                            showresult_during_keypressed=True
                                            oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                if oneloop:
                                                    view.draw()
                                                    oneloop=False
                                                view.show(model.rock)
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

                                            time=False
                                            
                                        elif event.key==K_s: ##Player chose scissors
                                            showresult_during_keypressed=True
                                            oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                if oneloop:
                                                    view.draw()
                                                    oneloop=False
                                                view.show(model.scissor)
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
                                            time=False
                                            
                                        elif event.key==K_p: ##Player chose paper
                                            showresult_during_keypressed=True
                                            oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                ##for one time it draws the background to hide the rockscissorpapaer popup
                                                if oneloop:
                                                    view.draw()
                                                    oneloop=False
                                                view.show(model.paper)
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
                                            time=False
                                    else:
                                        view.draw()
                                        view.show(model.attack)
                                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                controller.handle_key_event(event)

    view.draw()
    
    time.sleep(.050)
    sys.exit()
    pygame.quit()
