# Advent of Code Day 10 Puzzle 1

with open('day_10_puzzle_01_input.txt') as f:
    program = f.read().split('\n')


cycle = 1
x = 1
target_x = []
next_target_cycle = 20
for instrux in program:
    # print(f"CYCLE {cycle}")
    if instrux == 'noop':
        loop_num = 1
    else:
        loop_num = 2

    for i in range(loop_num):
        cycle += 1
        if i == 1:
            x += int(instrux.split(' ')[1])
        if cycle == next_target_cycle:
            # print(f"Cycle {cycle}, signal strength: {x} * {cycle} = {x*cycle}")
            target_x.append(x*cycle)
            next_target_cycle += 40


print(sum(target_x))
