from demo import PyGameSystem, GameLoop
from demo.engine import SequentialEngine


def test_sequential():
    system = PyGameSystem(GameLoop(), SequentialEngine(), dimension=(1_200, 700))
    system.start()
