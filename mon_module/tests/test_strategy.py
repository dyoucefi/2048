"""
Unit tests for ``random_strategy``.
"""
import unittest
import numpy
from pystrat2048.random_strategy import (
    random_strategy, random_strategy_all_but_one
)
from pystrat2048 import evaluate_strategy


class TestStrategy(unittest.TestCase):

    def test_random_strategy(self):
        rnd = random_strategy(numpy.zeros((4, 4), dtype=int))
        assert rnd in {0, 1, 2, 3}

    def test_measure_strategy(self):
        gen = evaluate_strategy(random_strategy)
        res = list(gen)
        assert isinstance(res, list)
        assert all(map(lambda x: x > 0, res))

    def test_measure_strategy_all_but_one(self):
        gen = evaluate_strategy(random_strategy_all_but_one)
        res = list(gen)
        assert isinstance(res, list)
        assert all(map(lambda x: x > 0, res))


if __name__ == '__main__':
    unittest.main()
