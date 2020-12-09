class Bootloader:
    def __init__(self,boot_code):
        self.boot_code = boot_code
    
    def run(self,start=0,initial_value=0):

        self.pos = start
        self.accumulator  = initial_value
        visited_lines = set()
        while True:
            if self.pos in visited_lines:
                raise RuntimeError(visited_lines)
            if self.pos == len(self.boot_code):
                raise StopIteration(self.accumulator)
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
    boot_code = puzzle_input.splitlines(False)
    bootloader = Bootloader(boot_code)
    visited = ()
    acc = None
    try:
        bootloader.run()
    except RuntimeError as error:
        visited = error.args[0]
    except StopAsyncIteration as error:
        acc = error.args[0]

    for line_nr in visited:
        if not boot_code[line_nr][:3] == "acc":
            boot_code_modified = boot_code[:]
            if boot_code_modified[line_nr][:3] == "jmp":
                boot_code_modified[line_nr] = boot_code_modified[line_nr].replace("jmp","nop")
            else:
                boot_code_modified[line_nr] = boot_code_modified[line_nr].replace("nop","jmp")

            bootloader = Bootloader(boot_code_modified)
            try:
                bootloader.run()
            except RuntimeError as error:
                pass
            except StopIteration as error:
                return error.args[0]

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))