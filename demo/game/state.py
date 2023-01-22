import threading
from dataclasses import dataclass, field
from typing import List, Tuple, SupportsFloat

PositionType = List[Tuple[SupportsFloat, SupportsFloat]]


@dataclass
class GameState:
    _positions: PositionType = field(default_factory=list)
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def update_particle_positions(self, positions: PositionType):
        with self._lock:
            self._positions = positions

    def get_particle_positions(self) -> PositionType:
        with self._lock:
            return self._positions
