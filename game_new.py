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
    
    #rsplist=[view.rock_obs,view.scissor_obs,view.paper_obs]
    #instantiate the model and view classes

    model = MapsolvingModel()
    view = PyGameWindowView(model,screen1)
    controller = PyGameKeyboardController(model)
    def rcs_draw(num):
        if event.type==KEYDOWN:                 
            if event.key==K_SPACE:
                ## change the global variable in function
                global showresult_during_keypressed
                showresult_during_keypressed=False
        else:
            print "draw"
            view.draw()
            
            ## show the pick of the computer accroding to the argument "num"
            show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
            view.show_draw_popup()
            show[num]()

    def rcs_win(num):
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE:
                model.change_background()
                model.change_obstacle()
                model.change_item()
                model.change_player_position()
                #view.draw()
                global showresult_during_keypressed
                showresult_during_keypressed=False
                global Time
                Time=False
                
                return showresult_during_keypressed
                #change item. change obstacle
                #change player position
        else:
            print "player win"
            print "press SPACE to go to second round"
            view.draw()
            #pygame.time.delay(500)
            show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
            view.show_win_popup()
            #view.show_scissor_obs()
            show[num]()
            return

    def rcs_lost(num):
    
                                                        
        if event.key==pygame.K_a:
            
            model.reset()
            global showresult_during_keypressed
            showresult_during_keypressed=False
            
            #restart
        else:
            print "player lost" #change it to graphics
            print "To play again press a"
            view.draw()
            
            show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
            view.show_lost_popup()
            show[num]()

    running = True
    while running:
        view.draw()

        #Picking up items: this should happen when you press the key for "pick up item" not automatically when you collide with it:
        if pygame.sprite.collide_rect(model.player, model.item):
            #
            model.player.pick_up_item(model.player, model.item)
            picked_up_item = True
            #picked_up_item = False

        ##Items are solid from the left
        if pygame.sprite.collide_rect(model.player, model.item):
            if model.player.previousx <= model.player.xposition:
                if picked_up_item:
                    pass
                else:
                    controller.model.player.stepback()
        ##Items are solid from the right
            elif model.player.previousx >= model.player.xposition:
                if picked_up_item:                  
                    pass
                else:                                        
                    controller.model.player.stepback()

        ##Obstacles are solid from the left
        ##THIS WILL BE MODIFIED SO THAT A SUCCESFUL BRIBE OR WIN IN A FIGHT WILL ALLOW YOU TO PASS
        if pygame.sprite.collide_rect(model.player, model.obstacle):
            obstcollision = True
            while obstcollision:
                view.show_popup()
                
                if model.player.previousx <= model.player.xposition:
                    controller.model.player.stepback()
                    
                elif model.player.previousx >= model.player.xposition:
                    controller.model.player.stepback()
            
            # pygame.time.delay(1000)

            # if model.player.previousx <= model.player.xposition:
            #     controller.model.player.moveleft()
            # elif model.player.previousx >= model.player.xposition:
            #     controller.model.player.moveright()
                for event in pygame.event.get():
                    if event.type==KEYDOWN: 
                        obstcollision = False
                        if even.key == K_i:

                        if event.key==K_f:
                            
                            ##showing the popup for the long time
                            rcnum=randint(0,2)#randomly pick the computer's rock//scissor//paper
                            Time=True
                            while Time:
                                for event in pygame.event.get():
                                    if event.type==KEYDOWN:
                                        
                                        ##when player pick rock(pressed R)
                                        if event.key==K_r: 
                                            ##rock image comes out and fight with randomly generated rock scissor paper of computer

                                            showresult_during_keypressed=True
                                            Oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                if Oneloop:
                                                    view.draw()
                                                    Oneloop=False
                                                view.show_rock()
                                                pygame.time.delay(50)
                                                if rcnum==0:
                                                    #rclist[rcnum]
                                                    #print "draw" #change this with graphics later on
                                                    for event in pygame.event.get():
                                                        rcs_draw(0)

                                                               
                                                elif rcnum==1:
                                                    for event in pygame.event.get():
                                                        
                                                        rcs_win(1)
                                                        print showresult_during_keypressed
                                                        # if showresult_during_keypressed==False:
                                                        #     Time=False
                                                        print Time

                                                        #showresult_during_keypressed=False


                                                #if computer's pick is paper
                                                elif rcnum==2:
                                                    for event in pygame.event.get():    
                                                        rcs_lost(2)


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
                                            """scissor image comes out and fight with randomly generated rock scissor paper of computer"""

                                            
                                            showresult_during_keypressed=True
                                            Oneloop=True
                                            while showresult_during_keypressed:
                                                
                                                if Oneloop:
                                                    view.draw()
                                                    Oneloop=False
                                                view.show_rock()
                                                pygame.time.delay(50)
                                                if rcnum==0:
                                                    #rclist[rcnum]
                                                    #print "draw" #change this with graphics later on
                                                    for event in pygame.event.get():
                                                        
                                                        if event.key==K_SPACE:
                                                            showresult_during_keypressed=False
                                                        else:
                                                            print "you lost"
                                                            view.draw()
                                                            pygame.time.delay(500)
                                                            view.show_lost_popup()
                                                            view.show_rock_obs()
                                                            
                                                            #view.show_draw
                                                            




                                                elif rcnum==1:
                                                    for event in pygame.event.get():

                                                        if event.key==pygame.K_SPACE:
                                                            model.change_background()
                                                            model.change_obstacle()
                                                            model.change_item()
                                                            model.change_player_position()

                                                            showresult_during_keypressed=False
                                                            Time=False
                                                            #change item. change obstacle
                                                            #change player position
                                                        else:
                                                            print "player draw"
                                                            print "press SPACE to go to second round"
                                                            view.draw()
                                                            pygame.time.delay(500)
                                                            view.show_win_popup()
                                                            view.show_scissor_obs()


                                                #if computer's pick is paper
                                                elif rcnum==2:
                                                    for event_new in pygame.event.get():
                                                        
                                                        if event_new.key==pygame.K_a:
                                                            
                                                            model.reset()
                                                            showresult_during_keypressed=False
                                                            
                                                            #restart
                                                        else:
                                                            print "player lost" #change it to graphics
                                                            print "To play again press a"
                                                            #view.draw()
                                                            #pygame.time.delay(500)
                                                            view.show_lost_popup()
                                                            view.show_paper_obs()
                                            Time=False
                                            
                                        elif event.key==K_p:
                                            Time=False
                                            view.show_paper
                                    else:
                                        view.draw()
                                        view.show_attack()
                                        print "show attack"

                                


                            
                   # else:
                


            
     
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
