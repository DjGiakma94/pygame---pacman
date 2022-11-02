from importlib import import_module

class GameMode:

    def __init__(self):
        self.name = ""
        self.scene = None

    def staticCreateFromDescriptor(descriptor):
        Type : str = descriptor["type"]

        # First parse the actor type which is in the form of path.to.component.Component
        gameModeModule, gameModeClass = Type.rsplit(".", 1)

        # load the module
        module = import_module(gameModeModule)
        
        # get a reference to the class
        c = getattr(module, gameModeClass)

        # create a component and defer the inialization to itself
        gameMode = c()
        gameMode.loadFromDescriptor(descriptor)

        return gameMode

    def loadFromDescriptor(self, descriptor):
        self.name = descriptor["name"]

    def setScene(self, scene):
        self.scene = scene



    def load(self):
        pass

    def unload(self):
        pass

    def update(self, deltaTime):
        pass

    def onDestroy(self):
        pass