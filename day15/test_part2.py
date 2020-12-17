import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input1(self):
        example_input = "0,3,6"
        self.assertEqual(solve_puzzle(example_input),175594)

    def test_example_input2(self):
        example_input = "1,3,2"
        self.assertEqual(solve_puzzle(example_input),2578)

    def test_example_input3(self):
        example_input = "2,1,3"
        self.assertEqual(solve_puzzle(example_input),3544142)

    def test_example_input4(self):
        example_input = "1,2,3"
        self.assertEqual(solve_puzzle(example_input),261214)

    def test_example_input5(self):
        example_input = "2,3,1"
        self.assertEqual(solve_puzzle(example_input),6895259)

    def test_example_input6(self):
        example_input = "3,2,1"
        self.assertEqual(solve_puzzle(example_input),18)

    def test_example_input7(self):
        example_input = "3,1,2"
        self.assertEqual(solve_puzzle(example_input),362)

