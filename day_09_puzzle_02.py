# Advent of Code 2022 Day 9 Puzzle 1
ropes_str = """......
......
......
......
H....."""

rope_bridge = [list(line) for line in ropes_str.split('\n')]

with open('day_09_puzzle_01_input.txt') as f:
    dirs = f.read().split('\n')

moves = [(line.split(' ')[0], int(line.split(' ')[1])) for line in dirs]
arbitrary_start = (0, 0)


def move_head(curr_spots, direction, visited_spots):
    curr_head_spot = curr_spots[0]
    if direction[0] == 'U':
        for i in range(direction[1]):
            curr_head_spot = (curr_head_spot[0]-1, curr_head_spot[1])
            curr_spots.pop(0)
            curr_spots.insert(0, curr_head_spot)
            for k in range(1, len(curr_spots)):
                curr_tail_spot = move_tail(curr_spots[k-1], curr_spots[k])
                curr_spots.pop(k)
                curr_spots.insert(k, curr_tail_spot)
                # print(f"HEAD: {curr_head_spot}, TAIL: {curr_tail_spot}")
            visited_spots.append(curr_tail_spot) if curr_tail_spot not in visited_spots else None
    elif direction[0] == 'L':
        for i in range(direction[1]):
            curr_head_spot = (curr_head_spot[0], curr_head_spot[1]-1)
            curr_spots.pop(0)
            curr_spots.insert(0, curr_head_spot)
            for k in range(1, len(curr_spots)):
                curr_tail_spot = move_tail(curr_spots[k-1], curr_spots[k])
                curr_spots.pop(k)
                curr_spots.insert(k, curr_tail_spot)
                # print(f"HEAD: {curr_head_spot}, TAIL: {curr_tail_spot}")
            visited_spots.append(curr_tail_spot) if curr_tail_spot not in visited_spots else None
    elif direction[0] == 'R':
        for i in range(direction[1]):
            curr_head_spot = (curr_head_spot[0], curr_head_spot[1]+1)
            curr_spots.pop(0)
            curr_spots.insert(0, curr_head_spot)
            for k in range(1, len(curr_spots)):
                curr_tail_spot = move_tail(curr_spots[k - 1], curr_spots[k])
                curr_spots.pop(k)
                curr_spots.insert(k, curr_tail_spot)
                # print(f"HEAD: {curr_head_spot}, TAIL: {curr_tail_spot}")
            visited_spots.append(curr_tail_spot) if curr_tail_spot not in visited_spots else None
    elif direction[0] == 'D':
        for i in range(direction[1]):
            curr_head_spot = (curr_head_spot[0]+1, curr_head_spot[1])
            curr_spots.pop(0)
            curr_spots.insert(0, curr_head_spot)
            for k in range(1, len(curr_spots)):
                curr_tail_spot = move_tail(curr_spots[k - 1], curr_spots[k])
                curr_spots.pop(k)
                curr_spots.insert(k, curr_tail_spot)
                # print(f"HEAD: {curr_head_spot}, TAIL: {curr_tail_spot}")
            visited_spots.append(curr_tail_spot) if curr_tail_spot not in visited_spots else None

    return curr_spots, visited_spots


def move_tail(curr_head_spot, curr_tail_spot):
    # ..T...
    # ....H.
    # ......
    # ......
    # ......
    # s.....
    # ......

    # Handle Diagonal movements
    if curr_head_spot[0] == curr_tail_spot[0]+2 and curr_head_spot[1] == curr_tail_spot[1]+1:
        curr_tail_spot = (curr_tail_spot[0]+1, curr_tail_spot[1]+1)
    elif curr_head_spot[0] == curr_tail_spot[0]-2 and curr_head_spot[1] == curr_tail_spot[1]+1:
        curr_tail_spot = (curr_tail_spot[0]-1, curr_tail_spot[1]+1)
    elif curr_head_spot[0] == curr_tail_spot[0]+2 and curr_head_spot[1] == curr_tail_spot[1]-1:
        curr_tail_spot = (curr_tail_spot[0]+1, curr_tail_spot[1]-1)
    elif curr_head_spot[0] == curr_tail_spot[0]-2 and curr_head_spot[1] == curr_tail_spot[1]-1:
        curr_tail_spot = (curr_tail_spot[0]-1, curr_tail_spot[1]-1)
    elif curr_head_spot[0] < curr_tail_spot[0] and curr_head_spot[1] < curr_tail_spot[1]-1:
        curr_tail_spot = (curr_tail_spot[0]-1, curr_tail_spot[1]-1)
    elif curr_head_spot[0] < curr_tail_spot[0] and curr_head_spot[1] > curr_tail_spot[1]+1:
        curr_tail_spot = (curr_tail_spot[0]-1, curr_tail_spot[1]+1)
    elif curr_head_spot[0] > curr_tail_spot[0] and curr_head_spot[1] > curr_tail_spot[1]+1:
        curr_tail_spot = (curr_tail_spot[0]+1, curr_tail_spot[1]+1)
    elif curr_head_spot[0] > curr_tail_spot[0] and curr_head_spot[1] < curr_tail_spot[1]-1:
        curr_tail_spot = (curr_tail_spot[0]+1, curr_tail_spot[1]-1)
    # Handle non-diagonal movements
    elif curr_head_spot[0] > curr_tail_spot[0]+1 and curr_head_spot[1] == curr_tail_spot[1]:
        curr_tail_spot = (curr_tail_spot[0]+1, curr_tail_spot[1])
    elif curr_head_spot[0] < curr_tail_spot[0]-1 and curr_head_spot[1] == curr_tail_spot[1]:
        curr_tail_spot = (curr_tail_spot[0]-1, curr_tail_spot[1])
    elif curr_head_spot[0] == curr_tail_spot[0] and curr_head_spot[1] > curr_tail_spot[1]+1:
        curr_tail_spot = (curr_tail_spot[0], curr_tail_spot[1]+1)
    elif curr_head_spot[0] == curr_tail_spot[0] and curr_head_spot[1] < curr_tail_spot[1]-1:
        curr_tail_spot = (curr_tail_spot[0], curr_tail_spot[1]-1)

    return curr_tail_spot


curr_spots = []
for i in range(10):
    curr_spots.append((15, 11))
spots_tail_visited = [(15, 11)]
for move in moves:
    # print(f"MOVE {move}")
    curr_spots, spots_tail_visited = move_head(curr_spots, move, spots_tail_visited)

# print(spots_tail_visited)
print(len(spots_tail_visited))

