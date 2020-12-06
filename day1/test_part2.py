import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_input = "1721\n979\n366\n299\n675\n1456"
        self.assertEqual(solve_puzzle(test_input),241861950)