import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """939
7,13,x,x,59,x,31,19"""
        self.assertEqual(solve_puzzle(example_input),5*59)
