import operator
from functools import reduce  

def solve_puzzle(puzzle_input):
    grid = puzzle_input.splitlines(False)
    row_length = len(grid[0])
    position = 0
    slopes = {  
        (1,1) : 0,
        (1,3) : 0,
        (1,5) : 0,
        (1,7) : 0,
        (2,1) : 0

    }
    for slope in slopes:
        position = 0
        for row in grid[::slope[0]]:
            if row[position % row_length] == "#":
                slopes[slope] += 1
            position += slope[1]
    return reduce(operator.mul,slopes.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))