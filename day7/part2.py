class BagNode:
    def __init__(self,colour):
        self.colour = colour
        self.is_in = []
        self.contains = []
        self.in_shiny_golden = False

class Counter:
    def __init__(self):
       self.value = 0

    def __call__(self):
        self.value += 1

count = 0

def mark_gold_shiny(current_bag,count,depth=0):
    count()
    for bag in current_bag["bag"].contains:
        # bag["bag"].in_shiny_golden = True
        if not bag["bag"].colour is None:
            for i in range(bag["nr"]):
                mark_gold_shiny(bag,count,depth+1)
    return count.value -1


def solve_puzzle(puzzle_input):
    global count
    node_dict = {}
    end_bags = set()

    for line in puzzle_input.splitlines(False):
        outer_bag, inner_bags = line.split(" contain ")
        outer_bag = outer_bag.replace(" bags","")
        if outer_bag in node_dict:
            parent_node = node_dict[outer_bag]
        else:
            parent_node = BagNode(outer_bag)
            node_dict[outer_bag] = parent_node
        for bag in inner_bags.split(", "):
            if bag.startswith("no"):
                nr = 0
                bag_colour = None
                end_bags.add(parent_node)
            else:
                tok = bag.split()
                nr = int(bag[0])
                bag_colour = " ".join(tok[1:-1])
            if bag_colour in node_dict:
                child_node = node_dict[bag_colour]
            else:
                child_node = BagNode(bag_colour)
                node_dict[bag_colour] = child_node
            child_node.is_in.append({"bag" : parent_node, "nr" : nr})
            parent_node.contains.append({"bag" : child_node, "nr" : nr})

    
    # 
    # print(node_dict)
    
    
    # for bag in end_bags:
    #     find_counts({"bag" : bag, "nr" : 1})
    return mark_gold_shiny({"bag" : node_dict["shiny gold"], "nr" : 1},Counter())

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))
