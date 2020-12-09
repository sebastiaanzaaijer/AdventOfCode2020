class Bootloader:
    def __init__(self,boot_code):
        self.boot_code = boot_code
    
    def run(self,start=0,initial_value=0):

        self.pos = start
        self.accumulator  = initial_value
        visited_lines = set()
        while True:
            if self.pos in visited_lines:
                return self.accumulator
            visited_lines.add(self.pos)
            instr, arg = self.boot_code[self.pos].split()
            arg = int(arg)
            getattr(self,instr)(arg)
    
    def nop(self,arg):
        self.pos += 1

    def acc(self,arg):
        self.accumulator += arg
        self.pos += 1

    def jmp(self,arg):
        self.pos += arg
            

def solve_puzzle(puzzle_input):
    bootloader = Bootloader(puzzle_input.splitlines(False))
    return bootloader.run()

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))