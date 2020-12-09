from part1 import solve_puzzle as solve_part1

def solve_puzzle(puzzle_input, invalid_nr):
    numbers = [int(x) for x in puzzle_input.splitlines(False)]
    N = len(numbers)
    for start_index in range(N):
        # print(start_index)
        number_sum = numbers[start_index]+numbers[start_index+1]
        for end_index in range(start_index+2,N):
            number_sum += numbers[end_index]
            if number_sum > invalid_nr:
                break
            if number_sum == invalid_nr:
                return min(numbers[start_index:end_index+1])+max(numbers[start_index:end_index+1])



if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input,solve_part1(puzzle_input)))