from demo import PyGameSystem, GameLoop
from demo.engine import StationaryEngine


def test_stationary():
    system = PyGameSystem(GameLoop(), StationaryEngine(), dimension=(1_200, 700), n_particles=150_000)
    system.start()
