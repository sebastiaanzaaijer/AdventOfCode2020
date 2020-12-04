import unittest

from .part2 import solve_puzzle

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

        self.assertEquals(solve_puzzle(test_data),336)