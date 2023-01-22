from dataclasses import dataclass

from lyrid import ActorSystem

from demo import PyGameLoop
from demo.core.common import Start
from demo.core.detector import CollisionDetector
from demo.core.game_loop import WaitForGameEnded


@dataclass
class PyGameSystem:
    game_loop: PyGameLoop
    detector: CollisionDetector

    def start(self):
        system = ActorSystem()

        game_loop_actor = system.spawn(self.game_loop.create_actor(), initial_message=Start())
        system.spawn(self.detector.create_actor(game_loop_actor), initial_message=Start())

        system.ask(game_loop_actor, WaitForGameEnded())

        system.force_stop()
