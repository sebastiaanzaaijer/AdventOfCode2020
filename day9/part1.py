def solve_puzzle(puzzle_input, preamble_length=25):
    numbers = [int(x) for x in puzzle_input.splitlines(False)]
    stack = numbers[:preamble_length]
    for number in numbers[preamble_length:]:
        valid = False
        for n in stack:
            if not n == number//2 and number-n in stack:
                valid = True
        if valid:
            stack.pop(0)
            stack.append(number)
        else:
            return number

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))