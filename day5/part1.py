def parse_boarding_pass(boarding_pass):
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)
    return row, col, row * 8 + col


def solve_puzzle(puzzle_input):
    id_max = 0
    for line in puzzle_input.splitlines(False):
        id_max = max(id_max,parse_boarding_pass(line)[2])
    return id_max


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
