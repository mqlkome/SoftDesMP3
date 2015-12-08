import pygame
from pygame.locals import *

# is this left over from something else?  I 
# don't think your game uses any kind of mouse motion?
class PyGameMouseController:
    def __init__(self,model):
        self.model = model
        def handle_mouse_event(self,event):
            if event.type == MOUSEMOTION:
                self.model.paddle.x = event.pos[0] - self.model.paddle.width/2.0

# this seems like all its functionality has been put into the game_new file
# this controller doesn't have much purpose
class PyGameKeyboardController:
    def __init__(self,model):
        self.model = model
    def handle_key_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == K_ESCAPE:
            pygame.quit()
        if event.key == pygame.K_LEFT:
            self.model.player.moveleft()
        if event.key == pygame.K_RIGHT:
            self.model.player.moveright()
        # if event.key ==pygame.K_f:
        #     self.model.popup.draw()
        