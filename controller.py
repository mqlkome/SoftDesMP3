import pygame
from pygame.locals import *

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
        if event.key == K_SPACE:
            if self.model.counter >3:
                pygame.quit()
        # if event.key ==pygame.K_f:
        #     self.model.popup.draw()
        