from dataclasses import dataclass
from typing import Optional

from lyrid import Actor, use_switch, switch, Address

from demo.core.common import Start
from demo.core.game_loop import WaitForGameEnded, GameEnded
from .loop import loop


@use_switch
@dataclass
class PyGameLoopActor(Actor):
    game_running: bool = False
    user_address: Optional[Address] = None
    user_ref_id: Optional[str] = None

    @switch.message(type=Start)
    def start(self):
        self.run_in_background(loop)
        self.game_running = True

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
