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
                if model.counter <=3:
                    model.change_background()
                    
                    model.change_item()
                    model.change_player_position()
                    model.change_obstacle()

                    #view.draw()
                    global showresult_during_keypressed
                    showresult_during_keypressed=False
                    #global Time
                    #Time=False
                    print model.counter
                    return showresult_during_keypressed
                    #change item. change obstacle
                    #change player position

                # elif model.counter==3:
                    
                #     model.change_background()
                    
                #     model.change_item()
                #     model.change_player_position()
                #     model.make_princess()
                      
                #     global showresult_during_keypressed
                #     showresult_during_keypressed=False
                    
                #     print model.counter
                #     return showresult_during_keypressed
                else:
                    print "you win final final"
                    pygame.quit()
                    
                        
                        

  
        else:
            if model.counter==4:
                view.draw()
                #pygame.time.delay(500)
                show=[view.show_rock_obs,view.show_scissor_obs,view.show_paper_obs]
                view.show_win_popup()
                #view.show_scissor_obs()
                show[num]()
                #pygame.time.delay(1000)
                view.show_final_popup()
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
                    


                #print "you win image this should be replace to image you won the princess"
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
                    controller.model.player.stepback()        ##Items are solid from the right
            elif model.player.previousx >= model.player.xposition:
                if picked_up_item:                  
                    pass
                else:                                        
                    controller.model.player.stepback()
        # if pygame.sprite.collide_rect(model.player, model.princess):
        #     print "player met princess"
        #     print "princess rect coor",model.princess.rect.x, model.princess.rect.y
        #     print "princess xy coord", model.princess.x,model.princess.y
        #     print "player xy coord", model.player.xposition, model.player.yposition
            
        ##Obstacles are solid from the left
        ##THIS WILL BE MODIFIED SO THAT A SUCCESFUL BRIBE OR WIN IN A FIGHT WILL ALLOW YOU TO PASS
        if pygame.sprite.collide_rect(model.player, model.obstacle): #or pygame.sprite.collide_rect(model.player, model.princess):
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
                            print (miip, one, two, three)
                            if miip == one or miip == two or miip == three:
                                view.show_thanks_popup()
                                pygame.display.update()
                                print "thanks"
                                pygame.time.delay(2000)
                                model.obstacle.move()
                                model.item.move()

                        
                            else:
                                view.show_nothanks_popup()
                                pygame.display.update()
                                print "no thanks"
                                pygame.time.delay(2000)
                                model.item.move()
                                
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
                                                        #print Time

                                                        #showresult_during_keypressed=False


                                                #if computer's pick is paper
                                                elif rcnum==2:
                                                    for event in pygame.event.get():    
                                                        rcs_lost(2)

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
                                                view.show_scissor()
                                                pygame.time.delay(50)
                                                if rcnum==0:
                                                    #rclist[rcnum]
                                                    #print "draw" #change this with graphics later on
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
                                                    #rclist[rcnum]
                                                    #print "draw" #change this with graphics later on
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
