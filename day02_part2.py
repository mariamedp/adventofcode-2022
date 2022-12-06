# fname = 'inputs/day02.test.txt'
fname = 'inputs/day02.txt'

with open(fname, 'r') as f:
    strategy = [l.strip().split(' ') for l in f.readlines()]

#     Rock: A
#    Paper: B
# Scissors: C

SHAPE_POINTS = {'A': 1, 'B': 2, 'C': 3}
WINNER = {'A': 'B', 'B': 'C', 'C': 'A'}
LOSER = {v: k for k, v in WINNER.items()}

points = 0
for opp, res in strategy:
    you = WINNER[opp] if res == 'Z' else opp if res == 'Y' else LOSER[opp]
    result_points = 6 if res == 'Z' else 3 if res == 'Y' else 0
    points += SHAPE_POINTS[you] + result_points

print(points)
