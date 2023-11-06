# Advent of Code 2022 Day 2 Puzzle 1
with open('day_02_puzzle_01_input.txt') as f:
    strategy_guide = f.read().split('\n')

strategy_guide_list = [line.split(' ') for line in strategy_guide]
# Key is what was played, value is what beats that
# A/X = Rock
# B/Y = Paper
# C/Z = Scissors
results_dict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
matching_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
points_dict = {'X': 1, 'Y': 2, 'Z': 3}

total_score = 0
for round in strategy_guide_list:
    if results_dict[round[0]] == round[1]:
        total_score += 6
        total_score += points_dict[round[1]]
    elif matching_dict[round[0]] == round[1]:
        total_score += 3
        total_score += points_dict[round[1]]
    else:
        total_score += points_dict[round[1]]

print(total_score)