def solve_puzzle(puzzle_input):

    # headings:
    headings = {
        0: (0,1), # North
        1: (1,0), # East
        2: (0,-1), # South
        3: (-1,0) # West
    }

    heading = 1
    position = [0,0]
    for action in puzzle_input.splitlines(False):
        move = action[:1]
        value = int(action[1:])
        if move == "L":
            heading = (heading - value//90) % 4
        if move == "R":
            heading = (heading + value//90) % 4
        if move == "N":
            position[1] += value
        if move == "S":
            position[1] -= value
        if move == "E":
            position[0] += value
        if move == "W":
            position[0] -= value
        if move == "F":
            d = headings[heading]
            position[0] = position[0]+d[0]*value
            position[1] = position[1]+d[1]*value

    return abs(position[0])+abs(position[1])

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))