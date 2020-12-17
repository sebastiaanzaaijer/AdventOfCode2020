def solve_puzzle(puzzle_input):
    mor = None
    mand = None
    memory = {}
    for line in puzzle_input.splitlines(False):
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            mor = int(mask.replace("X","0"),2)
            mand = int(mask.replace("X","1"),2)

        elif line.startswith("mem"):
            address,value = line.split("=")
            value = int(value.strip()) & mand | mor
            address = int(address.strip()[4:-1])
            memory[address] = value
        
    return sum(memory.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))