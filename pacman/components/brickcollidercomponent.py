from engine.components import *
from pygame.rect import Rect

class BrickColliderComponent(ColliderComponent):
    

    def onCollision(self, otherCollider):
        global listBrick
        if len(listBrick) == 3:
            #self.owner.destroy()
            listBrick.clear()
        