# fname = 'inputs/day04.test.txt'
fname = 'inputs/day04.txt'

with open(fname, 'r') as f:
    assignments = [l.strip() for l in f.readlines()]

count = 0
for range_pair in assignments:
    lowstart, highstart = sorted([tuple(int(id) for id in rg.split('-')) for rg in range_pair.split(',')])
    if lowstart[1] >= highstart[0]:
        count += 1

print(count)
