import random
from dataclasses import dataclass
from typing import Tuple

from lyrid import Actor, use_switch, switch, Address

from demo.core.common import Start
from demo.core.engine import CurrentParticlePositions
from demo.core.engine.message import DoUpdate


@use_switch
@dataclass
class SequentialEngineActor(Actor):
    game_loop_address: Address
    dimension: Tuple[int, int]

    @switch.message(type=Start)
    def start(self):
        self._schedule_next_update()

    @switch.message(type=DoUpdate)
    def update(self):
        self._schedule_next_update()

        positions = [(random.randint(0, self.dimension[0]), random.randint(0, self.dimension[1])) for _ in range(3)]
        self.tell(self.game_loop_address, CurrentParticlePositions(positions))

    def _schedule_next_update(self):
        self.tell(self.address, DoUpdate(), delay=1 / 15)
