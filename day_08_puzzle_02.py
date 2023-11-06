# Advent of Code 2022 Day 8 Puzzle 1
with open('day_08_puzzle_01_input.txt') as f:
    trees = f.read().split('\n')

tree_grid = [list(line) for line in trees]
tree_scenic_score = 0


def find_scenic_score(view1, view2, view3, view4):
    return view1 * view2 * view3 * view4


for t in range(len(tree_grid[0])):
    for i in range(len(tree_grid[0])):
        x = t
        y = i - 1
        target_tree = tree_grid[t][i]
        # print(f"TARGET TREE IS {tree_grid[t][i]} in tree row {tree_grid[t]}")
        # Check trees to left of target tree
        view1 = 0
        while y >= 0:
            view1 += 1
            if tree_grid[x][y] >= target_tree:
                break
            y -= 1
        # print(f"Can see {view1} trees to left")

        # Check trees to right of target tree
        y = i + 1
        view2 = 0
        while y < len(tree_grid[t]):
            view2 += 1
            if tree_grid[x][y] >= target_tree:
                break
            y += 1
        # print(f"Can see {view2} trees to right")

        # Check trees in column above target tree
        y = i
        x = t - 1
        view3 = 0
        while x >= 0:
            view3 += 1
            if tree_grid[x][y] >= target_tree:
                break
            x -= 1
        # print(f"Can see {view3} trees above")

        # Check trees in column below target tree
        x = t + 1
        view4 = 0
        while x < len(tree_grid):
            view4 += 1
            if tree_grid[x][y] >= target_tree:
                break
            x += 1
        # print(f"Can see {view4} trees below")

        scenic_score = find_scenic_score(view1, view2, view3, view4)
        if scenic_score > tree_scenic_score:
            tree_scenic_score = scenic_score

print(tree_scenic_score)
