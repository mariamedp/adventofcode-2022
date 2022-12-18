# fname = 'inputs/day08.test.txt'
fname = 'inputs/day08.txt'

with open(fname, 'r') as f:
    trees = [[int(t) for t in l.strip()] for l in f.readlines()]

rows = len(trees)
cols = len(trees[0])

views = [[[0, 0, 0, 0] for j in range(cols)] for i in range(rows)]


for i in range(rows):

    for j in range(cols):
        ntrees_seen = 0
        for jb in reversed(range(j)):
            ntrees_seen += 1
            if trees[i][j] <= trees[i][jb]:
                break
        views[i][j][0] = ntrees_seen

    for j in reversed(range(cols)):
        ntrees_seen = 0
        for jf in range(j+1, cols):
            ntrees_seen += 1
            if trees[i][j] <= trees[i][jf]:
                break
        views[i][j][1] = ntrees_seen

for j in range(cols):

    for i in range(rows):
        ntrees_seen = 0
        for ib in reversed(range(i)):
            ntrees_seen += 1
            if trees[i][j] <= trees[ib][j]:
                break
        views[i][j][2] = ntrees_seen

    for i in reversed(range(rows)):
        ntrees_seen = 0
        for ifw in range(i+1, rows):
            ntrees_seen += 1
            if trees[i][j] <= trees[ifw][j]:
                break
        views[i][j][3] = ntrees_seen

scenic_score = [[v[0] * v[1] * v[2] * v[3] for v in line] for line in views]

max(ssc for line in scenic_score for ssc in line)
