from ..component import Component
import pygame

class AnimatedSpriteComponent(Component):
    class Frame:
        def __init__(self, fileName, duration):
            self.fileName = fileName
            self.image = None
            self.duration = duration

    def __init__(self):
        super().__init__()
        self.frames = []
        self.pingPong = False
        self.pingPongDirection = 1
        self.currentFrame = 0
        self.currentTime = 0

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        self.pingPong = descriptor["pingPong"]
        fd = descriptor["frames"]
        for f in fd:
            frame = AnimatedSpriteComponent.Frame(f["fileName"], f["duration"])
            self.frames.append(frame)

    def load(self):
        for f in self.frames:
            f.image = pygame.image.load(f.fileName)

    def onDestroyed(self):
        for f in self.frames:
            f.image = None

    def update(self, deltaTime):
        self.currentTime += deltaTime

        # handles animation frame time independently to render frame time
        while self.currentTime > self.frames[self.currentFrame].duration:
            self.currentTime -= self.frames[self.currentFrame].duration
            
            self.goToNextFrame()

    def goToNextFrame(self):
        maxFrames = len(self.frames)
        nextFrame = 0
        if self.pingPong:
            nextFrame = self.currentFrame + self.pingPongDirection
            if nextFrame >= maxFrames:
                self.pingPongDirection = -1
                nextFrame = maxFrames - 2
            if nextFrame < 0:
                self.pingPongDirection = 1
                nextFrame = 1
        else:
            nextFrame = (self.currentFrame + 1) % maxFrames
        
        self.currentFrame = nextFrame

    def render(self, surface):
        f = self.frames[self.currentFrame]
        # ignore the frame size of the other images, the first one dictates the actual sprite size
        rect = self.frames[0].image.get_rect()
        rect.x = self.owner.x
        rect.y = self.owner.y
        surface.blit(f.image, rect)


