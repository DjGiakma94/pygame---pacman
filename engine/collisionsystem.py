class CollisionSystem:

    def __init__(self):
        self.colliders = []

    def reset(self):
        self.colliders.clear()

    def process(self):
        # detect collisions...

        for a in self.colliders:
            for b in self.colliders:
                if a is not b:
                    if a.AABB.colliderect(b.AABB):
                        a.onCollision(b)
                        

    def registerCollider(self, collider):
        self.colliders.append(collider)

    def deregisterCollider(self, collider):
        self.colliders.remove(collider)

    