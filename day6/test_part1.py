import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""
        self.assertEquals(solve_puzzle(example_input),11)
