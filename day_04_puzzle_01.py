# Advent of Code 2022 Day 4 Puzzle 1
with open('day_04_puzzle_01_input.txt') as f:
    assignments = f.read().split('\n')

total_contained = 0
for pair in assignments:
    pair_list = pair.split(',')
    p1 = pair_list[0].split('-')
    p2 = pair_list[1].split('-')
    assign1 = (int(p1[0]), int(p1[1]))
    assign2 = (int(p2[0]), int(p2[1]))
    if assign1[0] <= assign2[0] and assign1[1] >= assign2[1]:
        total_contained += 1
        if assign1 == (99, 99):
            print(f"IF ELIF: {assign1, assign2}")
    elif assign2[0] <= assign1[0] and assign2[1] >= assign1[1]:
        total_contained += 1
        if assign1 == (99, 99):
            print(f"FIRST ELIF: {assign1, assign2}")
    # elif assign2[0] == assign2[1] and (assign1[0] <= assign2[0] and assign1[1] >= assign2[1]):
    #     total_contained += 1
    #     if assign1 == (99, 99):
    #         print(f"PENULTIMATE ELIF: {assign1, assign2}")
    # elif assign1[0] == assign1[1] and (assign2[0] <= assign1[0] and assign2[1] >= assign1[1]):
    #     total_contained += 1
    #     if assign1 == (99, 99):
    #         print(f"LAST ELIF: {assign1, assign2}")

print(total_contained)
