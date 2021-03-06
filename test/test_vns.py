import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from Knapsack import Knapsack
from algorithms.vns import VNS


def test_shakes():
    INPUT_FILE = "test/testing_files/input1.txt"
    knap = Knapsack()
    knap.read_values(INPUT_FILE)

    vns = VNS(knap)

    tests = [
        ([0, 0, 0, 0, 0, 0],
         [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 1]]),
        ([0, 0, 0, 1, 0, 0],
         [[1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0],
          [0, 0, 0, 1, 0, 1]]),
        ([0, 0, 0, 0, 1, 1],
         [[1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0]])
    ]

    for test in tests:
        assert vns.shake(test[0]).tolist() in test[1]