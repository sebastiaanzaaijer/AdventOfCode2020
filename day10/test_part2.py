import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input1(self):
        example_input = """16
10
15
5
1
11
7
19
6
12
4"""
        self.assertEqual(solve_puzzle(example_input),8)

    def test_example_input2(self):
        example_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
        self.assertEqual(solve_puzzle(example_input),19208)
