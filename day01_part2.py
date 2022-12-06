# fname = 'inputs/day01.test.txt'
fname = 'inputs/day01.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

total_calories = [0]
for line in lines:
    if line == '':
        total_calories.append(0)
    else:
        total_calories[-1] += int(line)

print(sum(sorted(total_calories, reverse=True)[:3]))
