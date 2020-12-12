from collections import Counter
from itertools import groupby

from math import factorial
def number_of_permutations(n, r):
    return int(factorial(n)/factorial(n-r))

# hard coded number of posibilities 
# sultion won't work with than 4 consecutive adapters with 1 jolt difference
lookup = {
    1 : 1,
    2 : 2,
    3 : 4,
    4 : 7,
}


# for i in range(1,10):
#     print(i,number_of_posibilites(i))
def solve_puzzle(puzzle_input):
    adapters = sorted(int(x) for x in puzzle_input.splitlines(False))
    adapters.insert(0,0)# add 0 for outlet for first and last adapter
    adapters.append(adapters[-1]+3)
    differences = list(a-b for a,b in zip(adapters[1:],adapters[:-1]))
    posibilities = 1
    for k,g in groupby(differences):
        if k == 1:
            n = len(list(g))
            posibilities *= lookup[n]

    return posibilities

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))