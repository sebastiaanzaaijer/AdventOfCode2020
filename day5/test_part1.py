import unittest

from .part1 import solve_puzzle, parse_boarding_pass

class TestPuzzle(unittest.TestCase):

    def test_boarding_pass_parser(self):
        self.assertEqual(parse_boarding_pass("BFFFBBFRRR"),(70,7,567))
        self.assertEqual(parse_boarding_pass("FFFBBBFRRR"),(14,7,119))
        self.assertEqual(parse_boarding_pass("BBFFBBFRLL"),(102,4,820))
