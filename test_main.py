from demo import PyGameSystem, GameLoop
from demo.engine import StationaryEngine
from demo.no_engine import run_no_engine_brute_force


def test_no_engine_brute_force():
    run_no_engine_brute_force(dimension=(1_200, 700), n_particles=1_000, radius=5.)


def test_stationary():
    system = PyGameSystem(GameLoop(), StationaryEngine(), dimension=(1_200, 700), n_particles=1_000)
    system.start()
