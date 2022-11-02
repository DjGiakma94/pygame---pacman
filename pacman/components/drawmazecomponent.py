from engine.components import StaticSpriteComponent
import pygame
import pygame.locals

class DrawMazeComponent(StaticSpriteComponent):
    def __init__(self):
            super().__init__()
            self.rows = 10
            self.columns = 16
            self.maze = [   1,1,1,1,1,1,1,1,1,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,1,0,0,0,0,1,0,1,
                            1,0,1,1,0,1,0,1,0,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,0,0,1,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,0,1,1,1,0,1,1,0,1,
                            1,0,1,0,0,0,1,1,0,1,
                            1,0,0,0,1,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,1,1,1,1,1,1,1,1,1,]
            
    def loadFromDescriptor(self, descriptor):
        super().loadFromDescriptor(descriptor)
        self.assetMaze = descriptor["fileName"]

    def load(self):
           self._block_surf = pygame.image.load(self.assetMaze)

    def onDestroyed(self):
        self.image = None
         
    def render(self, surface):
        x = 0
        y = 0
        for i in range(0, len(self.maze)):
                if self.maze[i] == 1:
                    rect = self._block_surf.get_rect()
                    surface.blit(self._block_surf, (x * 40, y * 40))
                #coordinate for blit
                x += 1
                if x > self.rows-1:
                    x = 0 
                    y += 1
        
    