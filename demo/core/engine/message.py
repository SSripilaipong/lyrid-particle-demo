from dataclasses import dataclass
from typing import List, Tuple, SupportsFloat

from lyrid import Message


class DoUpdate(Message):
    pass


@dataclass
class CurrentParticlePositions(Message):
    positions: List[Tuple[SupportsFloat, SupportsFloat]]
