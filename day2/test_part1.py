import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
        self.assertEquals(solve_puzzle(test_data),2)