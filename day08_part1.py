# fname = 'inputs/day08.test.txt'
fname = 'inputs/day08.txt'

with open(fname, 'r') as f:
    trees = [[int(t) for t in l.strip()] for l in f.readlines()]

rows = len(trees)
cols = len(trees[0])

visible = [[False for j in range(cols)] for i in range(rows)]

for i in range(rows):
    maxheight = -1
    for j in range(cols):
        if trees[i][j] > maxheight:
            visible[i][j] = True
            maxheight = trees[i][j]
    maxheight = -1
    for j in range(cols-1, 0, -1):
        if trees[i][j] > maxheight:
            visible[i][j] = True
            maxheight = trees[i][j]

for j in range(cols):
    maxheight = -1
    for i in range(rows):
        if trees[i][j] > maxheight:
            visible[i][j] = True
            maxheight = trees[i][j]
    maxheight = -1
    for i in range(rows-1, 0, -1):
        if trees[i][j] > maxheight:
            visible[i][j] = True
            maxheight = trees[i][j]

sum(sum(line) for line in visible)
