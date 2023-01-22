from typing import Tuple

from lyrid import Address, Actor

from demo.core.engine import Engine
from demo.engine.stationary.actor import StationaryEngineActor


class StationaryEngine(Engine):

    def create_actor(self, game_loop_actor: Address, dimension: Tuple[int, int], n_particles: int) -> Actor:
        return StationaryEngineActor(game_loop_actor, dimension, n_particles)
