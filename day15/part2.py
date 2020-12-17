def solve_puzzle(puzzle_input):
    turn = 0
    spoken_nrs = {}
    for nr in puzzle_input.split(","):
        turn += 1
        spoken_nrs[int(nr)] = [turn,turn]

    last_nr = int(nr)

    while turn < 30000000:
        turn += 1
        last_time = spoken_nrs[last_nr]
        nr = last_time[1]-last_time[0]
        last_nr = nr
        if not nr in spoken_nrs:
            spoken_nrs[nr] = [turn,turn]
        spoken_nrs[nr].pop(0)
        spoken_nrs[nr].append(turn)
        # if turn % 10000 == 0:
        #     print(turn)
    return nr

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))