from itertools import combinations

def solve_puzzle(puzzle_input):
    expenses = set(int(x) for x in puzzle_input.splitlines(False))
    for x in expenses:
        if 2020-x in expenses:
            break
    return x*(2020-x)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))