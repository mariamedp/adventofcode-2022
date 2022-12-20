# fname = 'inputs/day10.test.txt'
fname = 'inputs/day10.txt'

with open(fname, 'r') as f:
    instructions = [l.strip() for l in f.readlines()]

X = 1
cycle = 0
signal_strength_snapshot = []


def increment(cycle):
    cycle += 1
    if cycle % 40 == 20:
        signal_strength_snapshot.append(cycle * X)
    return cycle


for instr in instructions:
    cycle = increment(cycle)
    if instr.startswith("addx "):
        cycle = increment(cycle)
        X += int(instr[5:])

sum(signal_strength_snapshot)
