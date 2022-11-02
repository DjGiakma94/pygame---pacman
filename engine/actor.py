from .component import Component
from importlib import import_module

class Actor:

    def __init__(self, scene):
        self.components = []
        self.x = 0
        self.y = 0
        self.name = ""
        self.scene = scene
        self.pendingDestroy = False

    def staticCreateFromDescriptor(descriptor, scene):
        actor : Actor = None
        if "type" in descriptor:
            actorType : str = descriptor["type"]

            # First parse the actor type which is in the form of path.to.component.Component
            actorModule, actorClass = actorType.rsplit(".", 1)

            # load the module
            module = import_module(actorModule)
            
            # get a reference to the class
            c = getattr(module, actorClass)

            # create a component and defer the inialization to itself
            actor = c(scene)
        else:
            # Use the generic actor class which is still useful for dumb actors that do nothing
            actor = Actor(scene)
        
        actor.loadFromDescriptor(descriptor)

        return actor

    def loadFromDescriptor(self, descriptor):
        self.name = descriptor["name"]
        self.x = descriptor["x"]
        self.y = descriptor["y"]
        
        if "components" not in descriptor:
            return
            
        for componentDescriptor in descriptor["components"]:
            component = Component.staticCreateFromDescriptor(componentDescriptor)
            if component is not None:
                self.addComponent(component)

    def load(self):
        for c in self.components:
            c.load()

    def destroy(self):
        self.pendingDestroy = True

    def onDestroyed(self):
        for c in self.components:
            c.onDestroyed()
        
        self.components = []

    def render(self, surface):
        for c in self.components:
            c.render(surface)

    # There will be timing involved
    def update(self, deltaTime):
        for c in self.components:
            c.update(deltaTime)
            
    def addComponent(self, component):
        self.components.append(component)
        component.setOwner(self)

    def findComponent(self, name):
        for c in self.components:
            if c.name == name:
                return c

        return None

