import math

def modular_inverse(a,n): 
    # assuming n is prime #https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

    return pow(a, n-2, n)



def solve_puzzle(puzzle_input):
    current_time, busses = puzzle_input.splitlines(False)
    current_time = int(current_time)

    bus_numbers,offsets = zip(*((int(bus),-i) for i,bus in enumerate(busses.split(",")) if bus != "x"))

    # chineese remainder theorem # https://www.dcode.fr/chinese-remainder
    n = 1
    for bus_number in bus_numbers:
        n *= bus_number
    
    time = 0
    for a_i,n_i in zip(offsets,bus_numbers):
        nhat_i = n//n_i
        v_i = modular_inverse(nhat_i,n_i)
        e_i = v_i * nhat_i
        time += a_i*e_i
    
    return time % n

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))