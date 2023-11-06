# Advent of Code 2022 Day 6 Puzzle 1
with open('day_06_puzzle_01_input.txt') as f:
    datastream = f.read()

for i in range(len(datastream)-3):
    recvd_chars = []
    recvd_chars.append(datastream[i])
    recvd_chars.append(datastream[i+1]) if datastream[i+1] not in recvd_chars else None
    recvd_chars.append(datastream[i+2]) if datastream[i+2] not in recvd_chars else None
    recvd_chars.append(datastream[i+3]) if datastream[i+3] not in recvd_chars else None
    if len(recvd_chars) == 4:
        print(i+4)
        break
