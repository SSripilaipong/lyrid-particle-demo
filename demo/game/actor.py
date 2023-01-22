from dataclasses import dataclass
from typing import Optional, Tuple

from lyrid import Actor, use_switch, switch, Address

from demo.core.common import Start
from demo.core.game_loop import WaitForGameEnded, GameEnded
from .loop import loop
from .state import GameState
from ..core.engine import CurrentParticlePositions


@use_switch
@dataclass
class GameLoopActor(Actor):
    dimension: Tuple[int, int]
    game_running: bool = False
    user_address: Optional[Address] = None
    user_ref_id: Optional[str] = None
    game_state: Optional[GameState] = None

    @switch.message(type=Start)
    def start(self):
        self.game_state = GameState()
        self.run_in_background(loop, args=(self.dimension, self.game_state))
        self.game_running = True

    @switch.message(type=CurrentParticlePositions)
    def update_particle_positions(self, message: CurrentParticlePositions):
        self.game_state.update_particle_positions(message.positions)

    @switch.ask(type=WaitForGameEnded)
    def wait_for_game_ended(self, sender: Address, ref_id: str):
        self.user_address = sender
        self.user_ref_id = ref_id

    @switch.background_task_exited(exception=None)
    def pygame_exited(self):
        self.game_running = False

    @switch.after_receive()
    def after_receive(self):
        if not self.game_running and self.user_address is not None and self.user_ref_id is not None:
            self.reply(self.user_address, GameEnded(), ref_id=self.user_ref_id)
