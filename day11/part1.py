class GameOfSeats:
    def __init__(self, layout):
        self.layout = layout
        self.previous_layout = None
        self.ni = len(layout)
        self.nj = len(layout[0])

    def current_state_at(self, i, j):
        if 0 <= i < self.ni and 0 <= j < self.nj:
            return self.layout[i][j]
        return "."

    def number_occupied_arround(self, i, j):
        n = 0
        for ii in range(-1, 2):
            for jj in range(-1, 2):
                if ii == 0 and jj == 0:
                    continue
                if self.current_state_at(i+ii, j+jj) == "#":
                    n += 1
        return n

        
    def next_state_at(self, i, j):
        if (
            self.current_state_at(i, j) == "L"
            and self.number_occupied_arround(i, j) == 0
        ):
            return "#"
        elif (
            self.current_state_at(i, j) == "#"
            and self.number_occupied_arround(i, j) >= 4
        ):
            return "L"
        return self.current_state_at(i, j)

    def step(self):
        new_layout = tuple(
            "".join(self.next_state_at(i, j) for j in range(self.nj))
            for i in range(self.ni)
        )
        self.previous_layout = self.layout
        self.layout = new_layout
        return self.layout
    
    def simulate(self):
        while not self.previous_layout == self.layout:
            self.step()

    def total_occupied(self):
        return "".join(self.layout).count("#")


def solve_puzzle(puzzle_input):
    game = GameOfSeats(tuple(puzzle_input.splitlines(False)))
    game.simulate()
    return game.total_occupied()

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path, "puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
