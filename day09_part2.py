# fname = 'inputs/day09.test2.txt'
fname = 'inputs/day09.txt'

with open(fname, 'r') as f:
    motions = [l.strip() for l in f.readlines()]

NKNOTS = 10

knots_poscs = [[0, 0] for i in range(NKNOTS)]

all_tail_poscs = set()


def update_poscs(head_posc, tail_posc):
    dist_horiz = head_posc[0] - tail_posc[0]
    dist_vert = head_posc[1] - tail_posc[1]
    if abs(dist_horiz) == 2 or (abs(dist_horiz) == 1 and abs(dist_vert) == 2):
        tail_posc[0] += dist_horiz // abs(dist_horiz)
    if abs(dist_vert) == 2 or (abs(dist_vert) == 1 and abs(dist_horiz) == 2):
        tail_posc[1] += dist_vert // abs(dist_vert)


for motion in motions:
    direction = motion[0]
    steps = int(motion[2:])
    for i in range(steps):
        # Move head
        if direction == 'R':
            knots_poscs[0][0] += 1
        elif direction == 'L':
            knots_poscs[0][0] -= 1
        elif direction == 'U':
            knots_poscs[0][1] += 1
        elif direction == 'D':
            knots_poscs[0][1] -= 1   

        # Update rest
        for kn in range(1, NKNOTS):
            update_poscs(knots_poscs[kn-1], knots_poscs[kn])

        all_tail_poscs.add('-'.join(str(p) for p in knots_poscs[-1]))

len(all_tail_poscs)
