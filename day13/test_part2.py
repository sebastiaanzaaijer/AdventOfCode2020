import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input1(self):
        example_input = "939\n7,13,x,x,59,x,31,19"
        self.assertEqual(solve_puzzle(example_input),1068781)

    def test_example_input2(self):
        example_input = "0\n17,x,13,19"
        self.assertEqual(solve_puzzle(example_input),3417)

    def test_example_input3(self):
        example_input = "0\n67,7,59,61"
        self.assertEqual(solve_puzzle(example_input),754018)

    def test_example_input4(self):
        example_input = "0\n67,7,x,59,61"
        self.assertEqual(solve_puzzle(example_input),1261476)

    def test_example_input5(self):
        example_input = "0\n1789,37,47,1889"
        self.assertEqual(solve_puzzle(example_input),1202161486)

