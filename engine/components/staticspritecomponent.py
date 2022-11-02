from ..component import Component
from engine.components import *
import pygame

class StaticSpriteComponent(Component):
    def __init__(self):
        super().__init__()
        self.assetFileName = ""
        self.assetGhost = ""
        self.image = None
        self.ghost = None
        global listBrick

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        self.assetFileName = descriptor["fileName"]
        self.assetGhost = descriptor["ghostBlue"]
        
    def load(self):
        self.ghost = pygame.image.load(self.assetGhost)
        self.image = pygame.image.load(self.assetFileName)

    def onDestroyed(self):
        self.image = None

    def render(self, surface):
        if len(listBrick) >= 4:
            rect = self.ghost.get_rect()
            rect.x = self.owner.x
            rect.y = self.owner.y
            surface.blit(self.ghost, rect)
        else:
            rect = self.image.get_rect()
            rect.x = self.owner.x
            rect.y = self.owner.y
            surface.blit(self.image, rect)


