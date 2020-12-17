import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input1(self):
        example_input = "1,3,2"
        self.assertEqual(solve_puzzle(example_input),1)

    def test_example_input2(self):
        example_input = "2,1,3"
        self.assertEqual(solve_puzzle(example_input),10)

    def test_example_input3(self):
        example_input = "1,2,3"
        self.assertEqual(solve_puzzle(example_input),27)

    def test_example_input4(self):
        example_input = "2,3,1"
        self.assertEqual(solve_puzzle(example_input),78)

    def test_example_input5(self):
        example_input = "3,2,1"
        self.assertEqual(solve_puzzle(example_input),438)

    def test_example_input6(self):
        example_input = "3,1,2"
        self.assertEqual(solve_puzzle(example_input),1836)

