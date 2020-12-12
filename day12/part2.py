def solve_puzzle(puzzle_input):

    # headings:
    rotations = {
        0: ((1, 0), (0, 1)),  # 0 deg right
        1: ((0, 1), (-1, 0)),  # 90 deg right
        2: ((-1, 0), (0, -1)),  # 180 deg right
        3: ((0, -1), (1, 0)),  # 270 deg right
    }

    waypoint = [10, 1]
    position = [0, 0]
    for action in puzzle_input.splitlines(False):
        move = action[:1]
        value = int(action[1:])
        if move == "L":
            move = "R"
            value = 360 - value
        if move == "R":
            r = rotations[(value // 90) % 4]
            new = [
                r[0][0] * waypoint[0] + r[0][1] * waypoint[1],
                r[1][0] * waypoint[0] + r[1][1] * waypoint[1],
            ]
            waypoint = new
        if move == "N":
            waypoint[1] += value
        if move == "S":
            waypoint[1] -= value
        if move == "E":
            waypoint[0] += value
        if move == "W":
            waypoint[0] -= value
        if move == "F":
            position[0] += waypoint[0]*value
            position[1] += waypoint[1]*value
    return abs(position[0]) + abs(position[1])


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
