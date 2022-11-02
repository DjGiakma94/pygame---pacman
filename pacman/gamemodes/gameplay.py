from engine.gamemode import GameMode
from engine.components.collidercomponent import *

class GamePlay(GameMode):

    def __init__(self):
        self.startingLives = 0
        self.lives = 0
        self.engine = None
        global lost

    def ballDropped(self):
        self.lives -= 1

    def loadFromDescriptor(self, descriptor):
        self.startingLives = descriptor["lives"]

    def load(self):
        from engine import Engine
        self.engine = Engine()
        self.reset()

    def reset(self):
        self.lives = self.startingLives

    def update(self, deltaTime):
        ghost = self.scene.findActor("ghost")

        if ghost is None:
            # there are no more bricks in the scene, you win!
            self.engine.loadScene("pacman/levels/start.json")

        if len(lost) == 0:
            self.engine.loadScene("pacman/levels/lost.json")
            
        if len(lost) == 3:
            self.engine.loadScene("pacman/levels/win.json")

    

        