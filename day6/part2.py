def solve_puzzle(puzzle_input):
    total = 0
    for group in puzzle_input.split("\n\n"):
        total += len(set("abcdefghijklmnopqrstuvwxyz").intersection(*(set(person) for person in group.splitlines(False))))
    return total

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))