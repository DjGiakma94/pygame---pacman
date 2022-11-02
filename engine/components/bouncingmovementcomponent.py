from ..component import *
from pygame.rect import Rect

class BouncingMovementComponent(Component):
    # Owner could be empty at first
    def __init__(self):
        super().__init__()
        self.vx = 0
        self.vy = 0
        self.boundingRect = Rect(0,0,0,0)

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        self.vx = descriptor["vx"]
        self.vy = descriptor["vy"]
        rd = descriptor["boundingRect"]
        self.boundingRect = Rect(rd["x"], rd["y"], rd["width"], rd["height"])

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    # There will be timing involved
    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.vx = -self.vx
        
        # bounce on the y axis
        if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
            self.vy = -self.vy