from dataclasses import dataclass

from demo import PyGameLoop
from demo.core import CollisionDetector


@dataclass
class PyGameSystem:
    game_loop: PyGameLoop
    detector: CollisionDetector

    def start(self):
        pass
