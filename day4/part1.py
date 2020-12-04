def solve_puzzle(puzzle_input):
    n_valid = 0
    mandatory_fields = set("byr iyr eyr hgt hcl ecl pid".split()) # not required cid 
    passports = [{y.split(":")[0]:y.split(":")[1] for y in x.replace("\n"," ").split()} for x in puzzle_input.split("\n\n")]
    for passport in passports:
        if len(mandatory_fields-set(passport)) == 0:
            n_valid += 1
    return n_valid

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))