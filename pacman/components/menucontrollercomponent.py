from engine.component import Component
import pygame.locals
from pygame.rect import Rect

class MenuControllerComponent(Component):
    def __init__(self):    
        from engine import Engine

        super().__init__()
        self.engine = Engine() # this is a singleton, don't worry too much
        self.engine.inputSystem.bindToKeyboard(pygame.locals.K_RETURN, self.keyPressed, onPress=True)

    def keyPressed(self, key):
        gamemode = self.engine.getGameMode()
        gamemode.nextPhase()
    