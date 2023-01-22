from lyrid import Address, Actor

from demo.core.detector import CollisionDetector
from demo.detector.sequential.actor import SequentialDetectorActor


class SequentialCollisionDetector(CollisionDetector):

    def create_actor(self, game_loop_actor: Address) -> Actor:
        return SequentialDetectorActor()
