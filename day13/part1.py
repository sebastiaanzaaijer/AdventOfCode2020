def solve_puzzle(puzzle_input):
    current_time, busses = puzzle_input.splitlines(False)
    current_time = int(current_time)
    busses = (int(bus) for bus in busses.split(",") if bus != "x" )
    min_wait_time = 999999999
    fastest_bus = None
    for bus in busses:
        earliest_departure = (current_time//bus+1)*bus
        wait_time = earliest_departure - current_time
        if wait_time < min_wait_time:
            fastest_bus = bus
            min_wait_time = wait_time
            
    return fastest_bus*min_wait_time


if __name__ == "__main__":
    import os
    import pathlib

    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
