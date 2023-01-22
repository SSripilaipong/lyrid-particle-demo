import random
from dataclasses import dataclass, field
from typing import Tuple, SupportsFloat, List

from lyrid import Actor, use_switch, switch, Address

from demo.core.common import Start
from demo.core.engine import CurrentParticlePositions
from demo.core.engine.message import DoUpdate


@use_switch
@dataclass
class StationaryEngineActor(Actor):
    game_loop_address: Address
    dimension: Tuple[int, int]
    n_particles: int

    positions: List[Tuple[SupportsFloat, SupportsFloat]] = field(default_factory=list)

    @switch.message(type=Start)
    def start(self):
        self._schedule_next_update()

        self.positions = [(random.randint(0, self.dimension[0]), random.randint(0, self.dimension[1]))
                          for _ in range(self.n_particles)]

    @switch.message(type=DoUpdate)
    def update(self):
        self._schedule_next_update()
        self.tell(self.game_loop_address, CurrentParticlePositions(self.positions))

    def _schedule_next_update(self):
        self.tell(self.address, DoUpdate(), delay=1 / 15)
