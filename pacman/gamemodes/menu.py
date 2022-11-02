from engine.gamemode import GameMode

class Menu(GameMode):

    def __init__(self):
        self.screen = ""
        self.engine = None

    def loadFromDescriptor(self, descriptor):
        self.screen = descriptor["screen"]

    def load(self):
        from engine import Engine
        self.engine = Engine()

    def nextPhase(self):
        if self.screen == "start":
            # we only manage level 1 here, the next levels will be loaded by the gameplay game mode
            self.engine.loadScene("pacman/levels/level1.json")
        elif self.screen == "lost":
            self.engine.loadScene("pacman/levels/start.json")
        

    

        