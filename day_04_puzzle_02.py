# Advent of Code 2022 Day 4 Puzzle 2
with open('day_04_puzzle_01_input.txt') as f:
    assignments = f.read().split('\n')

total_contained = 0
for pair in assignments:
    pair_list = pair.split(',')
    p1 = pair_list[0].split('-')
    p2 = pair_list[1].split('-')
    assign1 = (int(p1[0]), int(p1[1]))
    assign2 = (int(p2[0]), int(p2[1]))
    #5-7, 7-9
    #2-8, 3-7
    #6-6, 4-6
    #2-6, 4-8
    if assign2[0] <= assign1[1] <= assign2[1]:
        total_contained += 1
        print(assign1, assign2)
    elif assign1[0] <= assign2[1] <= assign1[1]:
        total_contained += 1


print(total_contained)
