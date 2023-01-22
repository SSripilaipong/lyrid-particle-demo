from typing import Tuple

from lyrid import Actor

from demo.game.actor import GameLoopActor


class GameLoop:

    @staticmethod
    def create_actor(dimension: Tuple[int, int]) -> Actor:
        return GameLoopActor(dimension)
