# Advent of Code 2022 Day 7 Puzzle 2
with open('day_07_puzzle_01_input.txt') as f:
    filesystem = f.read().split('\n')


def set_root_size(root_node):
    for child in root_node.children:
        root_node.size += child.size


def bubble_up_size(node, value_to_add):
    if node.parent.node_type == "root":
        return

    else:
        node.parent.size += value_to_add
        bubble_up_size(node.parent, value_to_add)


class TreeNode:
    def __init__(self, node_type=None, name=None, size=0, parent=None,
                 children=None):
        self.node_type = node_type
        self.name = name
        self.size = size
        self.parent = parent
        self.children = [] if children is None else children


root_node = TreeNode("root", "/")
current_dir = root_node
for line in filesystem:
    # Update current_dir
    if "$" == line.split(' ')[0] and "cd" == line.split(' ')[1]:
        curr_dir_name = line.split(' ')[2]
        if curr_dir_name == '..':
            current_dir = current_dir.parent
        else:
            for child in current_dir.children:
                if child.name == curr_dir_name:
                    current_dir = child

    # Add directory to root_node
    if "dir" == line.split(' ')[0]:
        node_name = str(line.split(' ')[1])
        node = TreeNode("dir", node_name, size=0, parent=current_dir)
        current_dir.children.append(node)
    # Add file to directory
    elif line.split(' ')[0].isdigit():
        node_name = str(line.split(' ')[1])
        node = TreeNode("file", node_name, int(line.split(' ')[0]),
                        parent=current_dir)
        current_dir.children.append(node)
        bubble_up_size(node, node.size)


set_root_size(root_node)


def print_tree(start_node, indents=0):
    print(f"|{'-'*(4*indents)}> {start_node.name} "
          f"({start_node.node_type}, {start_node.size})")

    if not start_node.children:
        return

    for node_child in start_node.children:
        print_tree(node_child, indents+1)


# print_tree(root_node)


def find_file_size(visited_nodes, q, sizes, space_needed=0):
    # Base case
    if not q:
        return

    node = q.pop(0)
    if node.node_type == 'dir' and node.size >= space_needed:
        sizes.append(node.size)

    for child in node.children:
        if child not in visited_nodes:
            visited_nodes.append(child)
            q.append(child)
            find_file_size(visited_nodes, q, sizes, space_needed)


filesystem_space_avail = 70000000
free_space = filesystem_space_avail - root_node.size
space_needed = 30000000 - free_space
visited = [root_node]
q = [root_node]
sizes = []
find_file_size(visited, q, sizes, space_needed)
print(min(sizes))
