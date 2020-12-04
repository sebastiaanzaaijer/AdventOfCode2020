def solve_puzzle(puzzle_input):
    n_valid = 0
    for line in puzzle_input.splitlines(False):
        policy,password = line.split(": ")
        minmax,letter = policy.split()
        nmin,nmax = (int(x) for x in minmax.split("-"))
        if nmin <= password.count(letter) <= nmax: n_valid += 1
    return n_valid

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))