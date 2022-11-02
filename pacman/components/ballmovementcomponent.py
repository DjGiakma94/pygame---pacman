from pygame import Vector2
from engine.components import ColliderComponent
import pygame.locals
import pygame
from ..gamemodes import GamePlay

class BallMovementComponent(ColliderComponent):
    
    def __init__(self):
        super().__init__()
        self.speed = 100
        self.v = Vector2(70, -71)

    def loadFromDescriptor(self, descriptor):
        # the AABB will be loaded by the parent ColliderComponent class
        super().loadFromDescriptor(descriptor)
        self.speed = descriptor["speed"]
        self.v.scale_to_length(self.speed)
                
    def load(self):
        from engine import Engine
        self.rect = pygame.Rect((41, 41), (329, 570))
        self.gamemode : GamePlay = Engine().getGameMode()
        super().load()


    def onCollision(self, otherCollider):
        # bounce on the collider
        # apply a spherical bounce, more or less
        a = self.AABB.center
        b = otherCollider.AABB.center

        self.v = Vector2(a[0] - b[0], a[1] - b[1])

        if abs(self.v.y) < 10:
            self.v.y = -10
        
        # conservation of momentum
        self.v.scale_to_length(self.speed)

    def update(self, deltaTime):
        super().update(deltaTime)

        self.owner.x += self.v.x * deltaTime
        self.owner.y += self.v.y * deltaTime

        if self.owner.x < self.rect.x:
            self.owner.x = self.rect.x + 1
            self.v.x *= -1

        if self.owner.x + self.AABB.width > self.rect.right:
            self.owner.x = self.rect.right - self.AABB.width - 1
            self.v.x *= -1

        if self.owner.y < self.rect.y:
            self.owner.y = self.rect.y + 1
            self.v.y *= -1

        if self.owner.y + self.AABB.height > self.rect.bottom:
            self.owner.y = self.rect.bottom - self.AABB.height - 1
            self.v.x *= -1