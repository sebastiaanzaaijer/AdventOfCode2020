from collections import Counter

def solve_puzzle(puzzle_input):
    adapters = sorted(int(x) for x in puzzle_input.splitlines(False))
    adapters.insert(0,0)# add 0 for outlet for first and last adapter
    adapters.append(adapters[-1]+3)
    differences = (a-b for a,b in zip(adapters[1:],adapters[:-1]))
    counts = Counter(differences)
    return counts[1]*counts[3]

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))