import threading
import time
from collections import deque
from dataclasses import dataclass, field
from typing import List, Tuple, SupportsFloat, Deque

PositionType = List[Tuple[SupportsFloat, SupportsFloat]]


@dataclass(frozen=True)
class RenderedGameState:
    positions: PositionType
    ups: float


@dataclass
class GameStateManager:
    _positions: PositionType = field(default_factory=list)
    _timestamps: Deque[float] = field(default_factory=deque)
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def update_particle_positions(self, positions: PositionType):
        timestamp = time.time()
        with self._lock:
            self._positions = positions

            self._timestamps.append(timestamp)
            if len(self._timestamps) > 30:
                self._timestamps.popleft()

    def render(self) -> RenderedGameState:
        with self._lock:
            positions = self._positions

            n_timestamps = len(self._timestamps)
            ups = (n_timestamps - 1) / (self._timestamps[-1] - self._timestamps[0]) if n_timestamps > 1 else 0.

        return RenderedGameState(positions=positions, ups=ups)
