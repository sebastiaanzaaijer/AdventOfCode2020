from collections import defaultdict


def get_bags(bag_dict,current_bag,unique_colors=set()):
    for bag in bag_dict[current_bag]:
        unique_colors.add(bag[0])
        get_bags(bag_dict,bag[0],unique_colors)
    return unique_colors


def solve_puzzle(puzzle_input):

    bag_in = defaultdict(list)

    for line in puzzle_input.splitlines(False):
        outer_bag, inner_bags = line.split(" contain ")
        outer_bag = outer_bag.replace(" bags","")
        for bag in inner_bags.split(", "):
            if bag.startswith("no"):
                nr = 0
                bag_colour = None
            else:
                tok = bag.split()
                nr = int(bag[0])
                bag_colour = " ".join(tok[1:-1])
            bag_in[bag_colour].append((outer_bag,nr))
    
    return len(get_bags(bag_in,"shiny gold"))

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))