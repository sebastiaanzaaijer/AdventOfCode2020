import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
        self.assertEqual(solve_puzzle(example_input),165)
