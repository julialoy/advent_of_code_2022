# Advent of Code 2022 Day 3 Puzzle 1
with open('day_03_puzzle_01_input.txt') as f:
    rucksacks = f.read().split('\n')

items = 'abcdefghijklmnopqrstuvwxyz'
priority_dict = {}

lower_count = 1
upper_count = 27
for i in items:
    priority_dict[i] = lower_count
    lower_count += 1
    priority_dict[i.upper()] = upper_count
    upper_count += 1


double_items = []
for rucksack in rucksacks:
    half = len(rucksack) // 2
    first_compartment = rucksack[:half]
    second_compartment = rucksack[half:]
    for item in first_compartment:
        if item in second_compartment:
            double_items.append(priority_dict[item])
            break

print(sum(double_items))

