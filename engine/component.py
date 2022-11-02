from importlib  import import_module



class Component:

    # Owner could be empty at first
    def __init__(self):
        self.name = ""
        self.owner = None
        

    def staticCreateFromDescriptor(descriptor):
        # First parse the component type which is in the form of path.to.component.Component
        compType : str = descriptor["type"]
        compModule, compClass = compType.rsplit(".", 1)

        # load the module
        module = import_module(compModule)
        
        # get a reference to the class
        c = getattr(module, compClass)

        # create a component and defer the inialization to itself
        component : Component = c()
        component.loadFromDescriptor(descriptor)

        return component

    def loadFromDescriptor(self, descriptor):
        self.name = descriptor["name"]

    def load(self):
        pass

    def onDestroyed(self):
        pass

    def render(self, surface):
        pass

    # There will be timing involved
    def update(self, deltaTime):
        pass

    def setOwner(self, actor):
        self.owner = actor
        
    def onCollision(self, otherCollider):
        pass