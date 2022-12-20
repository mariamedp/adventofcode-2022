# fname = 'inputs/day10.test.txt'
fname = 'inputs/day10.txt'

with open(fname, 'r') as f:
    instructions = [l.strip() for l in f.readlines()]


CRT = ''

X = 1
cycle = 0


def increment_cycle():
    global cycle, CRT
    cycle += 1

    pixel_horiz_posc = (cycle - 1) % 40
    if pixel_horiz_posc == 0:
        CRT += '\n'

    if X - 1 <= pixel_horiz_posc <= X + 1:
        CRT += '#'
    else:
        CRT += '.'


for instr in instructions:
    increment_cycle()
    if instr.startswith("addx "):
        increment_cycle()
        X += int(instr[5:])


print(CRT)

