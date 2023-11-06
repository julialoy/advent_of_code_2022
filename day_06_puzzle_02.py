# Advent of Code 2022 Day 6 Puzzle 1
with open('day_06_puzzle_01_input.txt') as f:
    datastream = f.read()

for i in range(len(datastream)-13):
    recvd_chars = []
    x = 0
    while x < 14:
        recvd_chars.append(datastream[i+x]) if datastream[i+x] not in recvd_chars else None
        x += 1
    if len(recvd_chars) == 14:
        print(f"First marker after char: {i+14}")
        break
