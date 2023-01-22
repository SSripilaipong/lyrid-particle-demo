from demo import PyGameSystem, PyGameLoop
from demo.engine import SequentialEngine


def test_sequential():
    system = PyGameSystem(PyGameLoop(), SequentialEngine())
    system.start()
