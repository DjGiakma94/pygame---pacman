from engine.components import *
import pygame.locals
from pygame.rect import Rect
from pygame import Vector2

class PlayerMovementComponent(ColliderComponent):
    def __init__(self):    
        global listBrick
        from engine import Engine

        super().__init__()
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.arrowPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.arrowPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_UP, self.arrowPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_DOWN, self.arrowPressed)
        

        self.vx = 0
        self.vy = 0
        self.speed = 0
        self.inertia = 0
        self.rect = Rect(0,0,0,0)
        self.AABB = Rect(0,0,0,0)
        self.a = 0
        self.b_width = 0
        self.b_height = 0
        

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        r = descriptor["AABB"]
        self.AABB = Rect(r["x"], r["y"], r["width"], r["height"])
        self.speed = descriptor["speed"]
        self.inertia = descriptor["inertia"]

    def load(self):
        from engine import Engine
        engine = Engine()
        self.rect = engine.window.get_rect()
        
    def arrowPressed(self, key):
        if key == pygame.locals.K_LEFT:
            self.vx = -self.speed
        if key == pygame.locals.K_RIGHT:
            self.vx = self.speed
        if key == pygame.locals.K_DOWN:
            self.vy = self.speed
        if key == pygame.locals.K_UP:
            self.vy = -self.speed
        
    """def onCollision(self, otherCollider):
        print("ciao")
        self.vx = 0
        self.vy = 0
        # bounce on the collider
        # apply a spherical bounce, more or less
        self.a = self.AABB.center
        print(otherCollider)
        self.b_width = otherCollider.AABB.width
        self.b_height = otherCollider.AABB.height"""
        

    def update(self, deltaTime):
        
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        # inertia
        if self.vx > 0:
            self.vx = self.vx - self.inertia * deltaTime
        if self.vx < 0:
            self.vx = self.vx + self.inertia * deltaTime
        # inertia
        if self.vy > 0:
            self.vy = self.vy - self.inertia * deltaTime
        if self.vy < 0:
            self.vy = self.vy + self.inertia * deltaTime

        

        # bounds
        if self.owner.x < 42:
            self.owner.x = 42
            self.vx = 0
        if self.owner.x + self.AABB.width > self.b_width:
            self.owner.x = self.b_width - self.AABB.width
            self.vx = 0
            
        # bounds
        if self.owner.y < 42:
            self.owner.y = 42
            self.vy = 0
        if self.owner.y + self.AABB.height > self.b_height:
            self.owner.y = self.b_height - self.AABB.height
            self.vx = 0
            
        if len(listBrick) == 1:
            #print(listBrick, "player")
            self.owner.y = self.owner.y - 10
            self.vy = 0
            self.owner.x = self.owner.x - 10
            self.vx = 0
            if 1<=len(listBrick)<4:
                listBrick.pop()
            #print(listBrick, "clear")

    def arrowPressed(self, key):
        if len(listBrick) != 1:
            if key == pygame.locals.K_LEFT:
                self.vx = -self.speed
            if key == pygame.locals.K_RIGHT:
                self.vx = self.speed
            if key == pygame.locals.K_DOWN:
                self.vy = self.speed
            if key == pygame.locals.K_UP:
                self.vy = -self.speed
        
        
            
    