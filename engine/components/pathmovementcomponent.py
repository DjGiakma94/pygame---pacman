import math
from ..component import Component

class PathMovementComponent(Component):

    class Leg:
        def __init__(self, x, y, time):
            self.x = x
            self.y = y
            self.time = time

    def __init__(self):
        super().__init__()
        self.path = []
        self.currentLeg = 0
        self.vx = 0
        self.vy = 0

    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        for l in descriptor["path"]:
            leg = PathMovementComponent.Leg(l["x"], l["y"], l["time"])
            self.path.append(leg)
            
    def load(self):
        self.goToLeg(0)

    def goToLeg(self, legNumber):
        if legNumber > len(self.path):
            return

        self.currentLeg = legNumber
        leg = self.path[self.currentLeg]

        # determine the new speed vx, vy to reach destination in the given timeframe
        if leg.time > 0:
            self.vx = (leg.x - self.owner.x) / leg.time
            self.vy = (leg.y - self.owner.y) / leg.time
        else:
            # teleport! yooooo!
            self.vx = 0
            self.vy = 0
            self.owner.x = leg.x
            self.owner.y = leg.y

    def update(self, deltaTime):
        leg = self.path[self.currentLeg]

        # move forward one step
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime

        # check to see if we reached destination
        distanceX = self.owner.x - leg.x
        distanceY = self.owner.y - leg.y
        dist = math.sqrt(distanceX ** 2 + distanceY ** 2)

        if dist < 1:            
            # ok, we are close enough, switch to the next leg
            self.goToLeg((self.currentLeg + 1) % len(self.path))
            


