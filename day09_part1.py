# fname = 'inputs/day09.test.txt'
fname = 'inputs/day09.txt'

with open(fname, 'r') as f:
    motions = [l.strip() for l in f.readlines()]

head_posc = [0, 0]
tail_posc = [0, 0]

all_tail_poscs = set()

def update_poscs():
    dist_horiz = head_posc[0] - tail_posc[0]
    dist_vert = head_posc[1] - tail_posc[1]
    if abs(dist_horiz) == 2 or (abs(dist_horiz) == 1 and abs(dist_vert) == 2):
        tail_posc[0] += dist_horiz // abs(dist_horiz)
    if abs(dist_vert) == 2 or (abs(dist_vert) == 1 and abs(dist_horiz) == 2):
        tail_posc[1] += dist_vert // abs(dist_vert)
    all_tail_poscs.add('-'.join(str(p) for p in tail_posc))


for motion in motions:
    direction = motion[0]
    steps = int(motion[2:])
    for i in range(steps):
        if direction == 'R':
            head_posc[0] += 1
        elif direction == 'L':
            head_posc[0] -= 1
        elif direction == 'U':
            head_posc[1] += 1
        elif direction == 'D':
            head_posc[1] -= 1
        update_poscs()

len(all_tail_poscs)
