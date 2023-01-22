from abc import ABC, abstractmethod
from typing import Tuple

from lyrid import Address, Actor


class Engine(ABC):

    @abstractmethod
    def create_actor(self, game_loop_actor: Address, dimension: Tuple[int, int], n_particles: int) -> Actor:
        pass
