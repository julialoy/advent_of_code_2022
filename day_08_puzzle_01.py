# Advent of Code 2022 Day 8 Puzzle 1
with open('day_08_puzzle_01_input.txt') as f:
    trees = f.read().split('\n')

tree_grid = [list(line) for line in trees]
visible_trees = len(tree_grid) * 2 + (len(tree_grid[0])-2) * 2
print(f"START WITH {visible_trees} visible")

for t in range(1, len(tree_grid[0])-1):
    for i in range(1, len(tree_grid[0])-1):
        x = t
        y = 0
        target_tree = tree_grid[t][i]
        # print(f"TARGET TREE IS {tree_grid[t][i]} in tree row {tree_grid[t]}")
        # Check trees to left of target treee
        while y < i:
            if tree_grid[x][y] >= target_tree:
                break
            y += 1
        if y == i:
            visible_trees += 1
            # print(f"Target tree visible to LEFT")
            continue

        # Check trees to right of target tree
        y = i+1
        while y < len(tree_grid[t]):
            # print(f"    Checking tree {tree_grid[x][y]}")
            if tree_grid[x][y] >= target_tree:
                break
            y += 1
        if y == len(tree_grid[t]):
            visible_trees += 1
            # print(f"Target tree visible to RIGHT")
            continue

        # Check trees in column above target tree
        y = i
        x = 0
        while x < t:
            if tree_grid[x][y] >= target_tree:
                break
            x += 1
        if x == t:
            visible_trees += 1
            # print(f"Target tree visible ABOVE")
            continue

        # Check trees in column below target tree
        x = t+1
        while x < len(tree_grid):
            if tree_grid[x][y] >= target_tree:
                break
            x += 1
        if x == len(tree_grid):
            visible_trees += 1
            # print(f"Target tree visible BELOW")
        # print(f"VISIBILE TREES: {visible_trees}")

print(visible_trees)