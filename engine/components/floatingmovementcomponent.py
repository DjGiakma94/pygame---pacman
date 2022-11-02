import pygame.locals
from ..component import Component

class FloatingMovementComponent(Component):
    def __init__(self):    
        from engine import Engine

        super().__init__()
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_UP, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_DOWN, self.keyPressed)

        self.vx = 0
        self.vy = 0

    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        # inertia
        if self.vx > 0:
            self.vx = self.vx - 100 * deltaTime
        if self.vx < 0:
            self.vx = self.vx + 100 * deltaTime
        if self.vy > 0:
            self.vy = self.vy - 100 * deltaTime
        if self.vy < 0:
            self.vy = self.vy + 100 * deltaTime
        

    def keyPressed(self, key):
        if key == pygame.locals.K_UP:
            self.vy = -100
        if key == pygame.locals.K_DOWN:
            self.vy = 100
        if key == pygame.locals.K_LEFT:
            self.vx = -100
        if key == pygame.locals.K_RIGHT:
            self.vx = 100
    