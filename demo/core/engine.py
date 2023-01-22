from abc import ABC, abstractmethod

from lyrid import Address, Actor


class Engine(ABC):

    @abstractmethod
    def create_actor(self, game_loop_actor: Address) -> Actor:
        pass
