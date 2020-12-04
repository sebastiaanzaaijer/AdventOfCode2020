from itertools import combinations

def solve_puzzle(puzzle_input):
    expenses = (int(x) for x in puzzle_input.splitlines(False))
    for combination in combinations(expenses,3):
        if sum(combination) == 2020:
            break
    return combination[0] * combination[1] * combination[2]

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))