def has_valid_fields(passport):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    for field in passport:
        if field == "byr" and not 1920 <= int(passport[field]) <= 2002: return False
        if field == "iyr" and not 2010 <= int(passport[field]) <= 2020: return False
        if field == "eyr" and not 2020 <= int(passport[field]) <= 2030: return False
        if field == "hgt":
            units = passport[field][-2:]
            try:
                height = int(passport[field][:-2])
            except ValueError:
                return False
            if not units in {"in","cm"}: return False
            if units == "cm" and not 150 <= height <= 193: return False
            if units == "in" and not 59 <= height <= 76: return False
        if field == "hcl":
            if not passport[field][0] == "#": return False
            if not len(passport[field][1:]) == 6: return False
            try:
                int(passport[field][1:],16)
            except ValueError:
                return False
        if field == "ecl" and not passport[field] in {"amb","blu","brn","gry","grn","hzl","oth"}: return False
        if field == "pid":
            if not len(passport[field]) == 9: return False
            try:
                int(passport[field])
            except ValueError:
                return False

    return True

def solve_puzzle(puzzle_input):
    n_valid = 0
    mandatory_fields = set("byr iyr eyr hgt hcl ecl pid".split()) # not required cid 
    passports = [{y.split(":")[0]:y.split(":")[1] for y in x.replace("\n"," ").split()} for x in puzzle_input.split("\n\n")]
    for passport in passports:
        if len(mandatory_fields-set(passport)) == 0 and has_valid_fields(passport):
            n_valid += 1
    return n_valid

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))