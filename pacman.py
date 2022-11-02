import sys
from engine.engine import Engine

# Global state variable
engine = Engine()


#engine.saveScene("pacman/levels/level2.json")
engine.loadScene("pacman/levels/start.json")

# game loop
engine.gameLoop()


sys.exit()