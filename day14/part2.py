from itertools import product

def solve_puzzle(puzzle_input):
    # TODO: use bit rather than string representation
    mor = None
    mand = None
    Xs = None
    mask = None
    memory = {}
    for line in puzzle_input.splitlines(False):
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            mor = int(mask.replace("X","0"),2)
            mand = int(mask.replace("X","1"),2)
            Xs = [i for i,x in enumerate(mask) if x == "X"]


        elif line.startswith("mem"):
            address,value = line.split("=")
            value = int(value.strip())
            address = "{:036b}".format(int(address.strip()[4:-1]))
            base_address = [a if m=="X" or m=="0" else m for a,m in zip(address,mask)]
            for comb in product(["0","1"],repeat=len(Xs)):
                address = base_address[:]
                for flip,pos in zip(comb,Xs):
                    address[pos] =flip
                address = int("".join(address),2)
                memory[address] = value
    return sum(memory.values())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))