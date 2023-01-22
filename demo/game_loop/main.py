from lyrid import Actor

from demo.game_loop.actor import PyGameLoopActor


class PyGameLoop:

    @staticmethod
    def create_actor() -> Actor:
        return PyGameLoopActor()
