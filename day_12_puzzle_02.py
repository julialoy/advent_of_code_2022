# Advent of Code 2022 Day 12 Puzzle 1
from math import inf

with open('day_12_puzzle_01_input.txt') as f:
    hill_lists = f.read().split('\n')
    hill_map = [list(line) for line in hill_lists]


start_coords= None
end_coords = None
for i in range(len(hill_map)):
    for x in range(len(hill_map[i])):
        if hill_map[i][x] == 'S':
            hill_map[i][x] = ord('a')-1
            start_coords = (i, x)
        elif hill_map[i][x] == 'E':
            hill_map[i][x] = ord('z')
            end_coords = (i, x)
        else:
            hill_map[i][x] = ord(hill_map[i][x])

visited = [start_coords]
curr_coords = start_coords
path = [start_coords]


# Below functions based on A* pseudocode from Wikipedia
def set_score(g: list) -> dict:
    g_dict = {}
    for i in range(len(g)):
        for j in range(len(g[i])):
            node = (i, j)
            g_dict[node] = inf

    return g_dict


def h(coord: tuple, goal: tuple) -> int:
    return abs(goal[0]-coord[0]) + abs(goal[1]-coord[1])


def reconstruct_path(came_from: dict, current: tuple) -> list:
    total_path = [current]
    while current[0] in came_from.keys():
        current = came_from[current[0]]
        total_path.insert(0, current[0])
    return total_path


def a_star_function(start: tuple, goal: tuple, graph: list, set_g_score=set_score, set_f_score=set_score, reconstruct_path=reconstruct_path, h=h) -> list:
    g_score = set_g_score(graph)
    g_score[start] = 0
    f_score = set_f_score(graph)
    f_score[start] = h(start, goal)

    open_set = [(start, f_score[start])]
    came_from = {}

    while open_set is not None:
        # Use of lambda for key from
        # https://stackoverflow.com/questions/14802128/tuple-pairs-finding-minimum-using-python
        try:
            current = min(open_set, key=lambda t: t[1])
        except ValueError:
            break
        if current[0] == goal:
            return reconstruct_path(came_from, current)
            # return came_from
        open_set.remove(current)
        tent_neighbor_list = []
        tent_neighbor_list.append((current[0][0]+1, current[0][1])) if current[0][0]+1 < len(graph) else None
        tent_neighbor_list.append((current[0][0]-1, current[0][1])) if current[0][0]-1 >= 0 else None
        tent_neighbor_list.append((current[0][0], current[0][1]+1)) if current[0][1]+1 < len(graph[current[0][0]]) else None
        tent_neighbor_list.append((current[0][0], current[0][1]-1)) if current[0][1]-1 >= 0 else None

        neighbor_list = []
        for neighbor in tent_neighbor_list:
            if hill_map[neighbor[0]][neighbor[1]] <= hill_map[current[0][0]][current[0][1]]+1:
                neighbor_list.append(neighbor)

        for neighbor in neighbor_list:
            tentative_g_score = g_score[current[0]] + (abs(current[0][0]-neighbor[0])+abs(current[0][1]-neighbor[1]))
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append((neighbor, f_score[neighbor]))

    return None


possible_path_lengths = []
for x in range(len(hill_map)):
    for y in range(len(hill_map[x])):
        if hill_map[x][y] == ord('a'):
            result = a_star_function((x, y), end_coords, hill_map)
            possible_path_lengths.append(len(result)-1) if result is not None else 0

print(possible_path_lengths)
print(min(possible_path_lengths))
