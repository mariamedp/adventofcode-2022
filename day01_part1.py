# fname = 'inputs/day01.test.txt'
fname = 'inputs/day01.txt'

with open(fname, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

total_calories, max_calories = 0, 0
for line in lines:
    if line == '':
        max_calories = max(total_calories, max_calories)
        total_calories = 0
    else:
        total_calories += int(line)

print(max_calories)
