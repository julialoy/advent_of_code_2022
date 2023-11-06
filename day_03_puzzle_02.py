# Advent of Code 2022 Day 3 Puzzle 1
with open('day_03_puzzle_01_input.txt') as f:
    rucksacks = f.read().split('\n')

grouped_rucksacks = []
for x in range(0, len(rucksacks), 3):
    group = [rucksacks[x], rucksacks[x+1], rucksacks[x+2]]
    grouped_rucksacks.append(group)

items = 'abcdefghijklmnopqrstuvwxyz'
priority_dict = {}

lower_count = 1
upper_count = 27
for i in items:
    priority_dict[i] = lower_count
    lower_count += 1
    priority_dict[i.upper()] = upper_count
    upper_count += 1


badges = []
for g in grouped_rucksacks:
    for item in g[0]:
        if item in g[1] and item in g[2]:
            badges.append(priority_dict[item])
            break

print(sum(badges))

