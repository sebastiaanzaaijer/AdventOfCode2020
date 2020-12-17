import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
        self.assertEqual(solve_puzzle(example_input),208)
