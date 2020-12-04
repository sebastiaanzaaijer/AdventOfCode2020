def solve_puzzle(puzzle_input):
    grid = puzzle_input.splitlines(False)
    row_length = len(grid[0])
    position = 0
    trees = 0
    for row in grid:
        if row[position % row_length] == "#":
            trees += 1
        position += 3

    return trees

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))