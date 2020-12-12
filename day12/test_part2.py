import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """F10
N3
F7
R90
F11"""
        self.assertEqual(solve_puzzle(example_input),214+72)
