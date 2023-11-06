# Advent of Code 2022 Day 1, Puzzle 2

with open('day_01_puzzle_01_input.txt') as f:
    total_elf_calories = f.read()

total_calories_list = list(total_elf_calories.split('\n\n'))
summed_list = []
for item in total_calories_list:
    sub_list_strs = list(item.split('\n'))
    sub_list_ints = [int(cals) for cals in sub_list_strs]
    summed_list.append(sum(sub_list_ints))

max_cals_list = []
while len(max_cals_list) < 3:
    max_item = max(summed_list)
    max_cals_list.append(max_item)
    summed_list.remove(max_item)

print(sum(max_cals_list))
