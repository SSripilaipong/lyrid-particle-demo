from lyrid import Address, Actor

from demo.core.engine import Engine
from demo.engine.sequential.actor import SequentialEngineActor


class SequentialEngine(Engine):

    def create_actor(self, game_loop_actor: Address) -> Actor:
        return SequentialEngineActor()
