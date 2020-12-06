import unittest

from .part2 import solve_puzzle, has_valid_fields

class TestValidator(unittest.TestCase):
    def test_validator(self):
        self.assertTrue(has_valid_fields({"byr":"2002"}))
        self.assertFalse(has_valid_fields({"byr":"2003"}))

        self.assertTrue(has_valid_fields({"hgt":"60in"}))
        self.assertTrue(has_valid_fields({"hgt":"190cm"}))
        self.assertFalse(has_valid_fields({"hgt":"190in"}))
        self.assertFalse(has_valid_fields({"hgt":"190"}))

        self.assertTrue(has_valid_fields({"hcl":"#123abc"}))
        self.assertFalse(has_valid_fields({"hcl":"#123abz"}))
        self.assertFalse(has_valid_fields({"hcl":"123abc"}))

        self.assertTrue(has_valid_fields({"ecl":"brn"}))
        self.assertFalse(has_valid_fields({"ecl":"wat"}))

        self.assertTrue(has_valid_fields({"pid":"000000001"}))
        self.assertFalse(has_valid_fields({"pid":"0123456789"}))

class TestPuzzle(unittest.TestCase):
    def test_invalid(self):
        example_input = """
        eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

        self.assertEqual(solve_puzzle(example_input),0)

    def test_valid(self):
        example_input = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
        self.assertEqual(solve_puzzle(example_input),4)

