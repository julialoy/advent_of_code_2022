# Advent of Code 2022 Day 13 Puzzle 1
with open('day_13_puzzle_01_input.txt') as f:
    packets = f.read().split('\n\n')

# [1,1,3,1,1] vs. [1,1,5,1,1]
# Both left and right are lists
# Compare 1 vs 1
# compare 1 vs 1
# Compare 3 vs 5 -> At this point we see left side is smaller
#
# [[1],[2,3,4]] vs [[1],4]
# Compare [1] vs [1]
#       Compare 1 vs 1
# Compare [2, 3, 4] vs 4
#   Convert right to [4
#   Compare [2, 3, 4] to [4]
#       Compare 2 vs 4 -> At this point we see left side is smaller
#
# [9] vs. [[8,7,6]]
# Compare [9] vs [[8, 7, 6]]
#   Compare 9 vs [8, 7, 6]
#   Conver 9 to [9]
#       Compare [9] vs [8, 7, 6]
#           Compare 9 vs 8 -> At this point we see right side is smaller
#
# [[4,4],4,4] vs. [[4,4],4,4,4]
#
# [7,7,7,7] vs. [7,7,7]
#
# [] vs. [3]
#
# [[[]]] vs. [[]]
#
# [1,[2,[3,[4,[5,6,7]]]],8,9] vs. [1,[2,[3,[4,[5,6,0]]]],8,9]

pair_indices = []
for pair in packets:
    left = pair[0]
    right = pair[1]
    i = 0
    while i < len(left):
        if type(left[i]) == list and type(right[i]) == list and len(left[i]) >= 1 and len(right[i]) >= 1:
            i += 1
            continue
        elif type(left[i]) == list and type(right[i]) == list and len(left[i]) == 0 and len(right[i]) >= 1:
            pair_indices.append(packets.index(pair)+1)
            i += 1
        elif type(left[i]) == list and type(right[i]) == list and len(left[i]) >= 1 and len(right[i]) == 0:
            break
        elif type(left[i]) != list and type(right[i]) == list:
            left[i] = [left[i]]
            continue
        elif type(left[i]) != list and type(right[i]) != list:
            if left < right:
                pair_indices.append(packets.index(pair)+1)
                i += 1
            elif left == right:
                i += 1
            else:
                break

print(pair_indices)


