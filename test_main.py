from demo import PyGameSystem, PyGameLoop
from demo.detector import SequentialCollisionDetector


def test_sequential():
    system = PyGameSystem(PyGameLoop(), SequentialCollisionDetector())
    system.start()
