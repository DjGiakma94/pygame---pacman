from pygame import rect
from .actor import Actor
from .gamemode import GameMode
import json

class Scene:

    def __init__(self):
        # there will be actors acting things
        self.actors = []
        self.windowRect = rect.Rect(0,0,0,0)
        self.scale = 0
        self.background = (0, 0, 0)
        self.title = ""
        self.gamemode : GameMode = None

    def staticCreateFromFile(fileName):
        with open(fileName, "r") as f:
            # this is a dictionary
            sceneDescriptor = json.load(f)

            scene = Scene()
            scene.loadFromDescriptor(sceneDescriptor)

            return scene
                

    def loadFromDescriptor(self, descriptor):
        w = descriptor["window"]
        self.windowRect.height = w["height"]
        self.windowRect.width = w["width"]
        self.scale = w["scale"] if "scale" in w else 1
        
        if "background" in w:
            c = w["background"]
            r,g,b = c["r"], c["g"], c["b"]
            self.background = (r,g,b)
        
        self.title = w["title"]
        if "gameMode" in descriptor:
            self.gamemode = GameMode.staticCreateFromDescriptor(descriptor["gameMode"])
        else:
            self.gamemode = GameMode()

        self.gamemode.setScene(self)

        for actorDescriptor in descriptor["actors"]:
            actor = Actor.staticCreateFromDescriptor(actorDescriptor, self)

            self.actors.append(actor)

    def load(self):
        for a in self.actors:
            a.load()

        self.gamemode.load()

    def unload(self):
        self.gamemode.unload()

        for a in self.actors:
            a.onDestroyed()

        self.actors = []

    def render(self, surface):
        # clear the screen
        surface.fill(self.background)

        for a in self.actors:
            a.render(surface)

    def update(self, deltaTime):
        toBeDestroyed = []
        for a in self.actors:
            if not a.pendingDestroy:
                a.update(deltaTime)
            else:
                toBeDestroyed.append(a)
        
        for a in toBeDestroyed:
            a.onDestroyed()
            self.actors.remove(a)

        self.gamemode.update(deltaTime)


    def findActor(self, name):
        for a in self.actors:
            if a.name == name:
                return a
        
        return None