# Advent of Code Day 10 Puzzle 1

with open('day_10_puzzle_01_input.txt') as f:
    program = f.read().split('\n')


cycle = 1
x = 1
sprite_pos = [x-1, x, x+1]
crt = []
crt_line = []
curs_pos = len(crt_line)
for instrux in program:
    if instrux == 'noop':
        loop_num = 1
    else:
        loop_num = 2

    for i in range(loop_num):
        # print(f" CYCLE: {cycle} X: {x} SPRITE: {sprite_pos}")
        if curs_pos in sprite_pos:
            crt_line.append('#')
        else:
            crt_line.append('.')

        if i == 1:
            x += int(instrux.split(' ')[1])
            sprite_pos = [x-1, x, x+1]

        if cycle % 40 == 0:
            crt.append(crt_line)
            crt_line = []

        cycle += 1
        curs_pos = len(crt_line)



for line in crt:
    print(' '.join(line))
