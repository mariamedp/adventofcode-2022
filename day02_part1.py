# fname = 'inputs/day02.test.txt'
fname = 'inputs/day02.txt'

with open(fname, 'r') as f:
    strategy = [l.strip().split(' ') for l in f.readlines()]

#     Rock: A / X
#    Paper: B / Y
# Scissors: C / Z

SHAPE_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
WINNER = {'A': 'Y', 'B': 'Z', 'C': 'X'}
TIE = {'A': 'X', 'B': 'Y', 'C': 'Z'}

points = 0
for opp, you in strategy:
    result_points = 6 if WINNER[opp] == you else 3 if TIE[opp] == you else 0
    points += SHAPE_POINTS[you] + result_points

print(points)
