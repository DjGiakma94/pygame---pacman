from ..component import Component
from pygame.rect import Rect

listBrick = []
lost = [1]
class ColliderComponent(Component):

    def __init__(self):
        super().__init__()
        self.AABB = Rect(0,0,0,0)
        self.originalAABB = Rect(0,0,0,0)
        self.vx = 0
        self.vy = 0
        global listBrick
        global lost

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        rd = descriptor["AABB"]
        self.AABB = Rect(rd["x"], rd["y"], rd["width"], rd["height"])
        self.originalAABB = Rect(rd["x"], rd["y"], rd["width"], rd["height"])

    def load(self):
        super().load()
        from engine import Engine
        self.collisionSystem = Engine().collisionSystem
        self.collisionSystem.registerCollider(self)
        self.update(0)

    def onDestroyed(self):
        pass

    def update(self, deltaTime):
        self.AABB.x = self.originalAABB.x + self.owner.x 
        self.AABB.y = self.originalAABB.y + self.owner.y

    def onCollision(self, otherCollider):
        if self.name == "collision-player" and otherCollider.name == "collision":
            if len(listBrick) == 0:
                listBrick.append(1)
            
        if self.name == "collision-player" and otherCollider.name == "movement-ghost":
            if len(listBrick)==0:
                listBrick.append(1)
            if len(listBrick)==1:
                self.owner.destroy()
                lost.clear()
            
        #when ghosy is blue
        if self.name == "ghost-coll" and otherCollider.name == "collision-player":
            if len(listBrick)>=4:
                self.owner.destroy()
                listBrick.clear()
                listBrick.append(1)
                listBrick.append(1)
                lost.append(1)
                
                
            
        if self.name == "red1" and otherCollider.name == "collision-player":
            if len(listBrick)<4:
                listBrick.append(1)
                listBrick.append(1)
                listBrick.append(1)
                listBrick.append(1)
                self.owner.destroy()
            
        if self.name == "red2" and otherCollider.name == "collision-player":
            listBrick.append(1)
            listBrick.append(1)
            listBrick.append(1)
            listBrick.append(1)
            self.owner.destroy()

    