import sys
from engine.engine import Engine

# Global state variable
engine = Engine()

engine.loadScene("demo.json")

# game loop
engine.gameLoop()

sys.exit()