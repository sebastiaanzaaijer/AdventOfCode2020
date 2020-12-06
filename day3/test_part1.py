import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

        self.assertEqual(solve_puzzle(test_data),7)
