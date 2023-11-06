# Advent of Code 2022 Day 5 Puzzle 2
with open('day_05_puzzle_01_input.txt') as f:
    crate_arrang, crate_proc = f.read().split('\n\n')

crate_arrang = crate_arrang.split('\n')
num_rows = int(crate_arrang[-1][-2])
crate_arrang = crate_arrang[:-1]
crates = []
for row in crate_arrang:
    new_row = []
    i = 1
    while i < len(row):
        if row[i].isalpha():
            new_row.append(row[i])
        else:
            new_row.append(' ')
        i += 4
    while len(new_row) < num_rows:
        new_row.append(' ')
    crates.append(new_row)

stacks = []
x = 0
while x < num_rows:
    stack = []
    for i in range(len(crates)-1, -1, -1):
        if crates[i][x] != ' ':
            stack.append(crates[i][x])
    stacks.append(stack)
    x += 1

crate_proc_list = crate_proc.split('\n')
instrux = []
for row in crate_proc_list:
    split_row = row.split(' ')
    new_row = [int(item) for item in split_row if item.isdigit()]
    instrux.append(new_row)

for row in instrux:
    i = row[0]
    from_stack = stacks[row[1] - 1]
    to_stack = stacks[row[2] - 1]
    if i == 1:
        item = from_stack.pop()
        to_stack.append(item)
    else:
        items = []
        for y in range(i):
            item = from_stack.pop()
            items.insert(0, item)
        for x in range(len(items)):
            to_stack.append(items[x])

top_crates = []
for stack in stacks:
    top_crates.append(stack.pop())

print(top_crates)

