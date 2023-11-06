# Advent of Code 2022 Day 2 Puzzle 2
with open('day_02_puzzle_01_input.txt') as f:
    strategy_guide = f.read().split('\n')

strategy_guide_list = [line.split(' ') for line in strategy_guide]
# Key is what was played, value is what beats that
# A/X = Rock
# B/Y = Paper
# C/Z = Scissors
winning_dict = {'A': 'B', 'B': 'C', 'C': 'A'}
losing_dict = {'A': 'C', 'B': 'A', 'C': 'B'}
# matching_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points_dict = {'A': 1, 'B': 2, 'C': 3}

total_score = 0
for round in strategy_guide_list:
    if round[1] == 'X':
        total_score += points_dict[losing_dict[round[0]]]
    elif round[1] == 'Y':
        total_score += 3
        total_score += points_dict[round[0]]
    elif round[1] == 'Z':
        total_score += 6
        total_score += points_dict[winning_dict[round[0]]]

print(total_score)
