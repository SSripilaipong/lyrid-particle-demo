from dataclasses import dataclass
from typing import Tuple

from lyrid import ActorSystem

from demo import GameLoop
from demo.core.common import Start
from demo.core.engine import Engine
from demo.core.game_loop import WaitForGameEnded


@dataclass
class PyGameSystem:
    game_loop: GameLoop
    engine: Engine
    dimension: Tuple[int, int]

    def start(self):
        system = ActorSystem()

        game_loop_actor = system.spawn(self.game_loop.create_actor(self.dimension), initial_message=Start())
        system.spawn(self.engine.create_actor(game_loop_actor, self.dimension), initial_message=Start())

        system.ask(game_loop_actor, WaitForGameEnded())

        system.force_stop()
