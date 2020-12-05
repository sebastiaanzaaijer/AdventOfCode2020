from part1 import parse_boarding_pass
from part1 import solve_puzzle as solve_part1

def solve_puzzle(puzzle_input):
    max_id = solve_part1(puzzle_input)
    available_seats = set(range(0,max_id+1))
    for line in puzzle_input.splitlines(False):
        available_seats.remove(parse_boarding_pass(line)[2])
    available_seats = sorted(available_seats)
    last_seat_id = available_seats.pop(0)
    for seat_id in available_seats:
        if seat_id - last_seat_id > 1:
            return seat_id
        last_seat_id = seat_id

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))