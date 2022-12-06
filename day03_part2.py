# fname = 'inputs/day03.test.txt'
fname = 'inputs/day03.txt'

with open(fname, 'r') as f:
    rucksacks = [l.strip() for l in f.readlines()]

priorities = []
group = []
for content in rucksacks:
    group.append(set(content))
    if len(group) == 3:
        item = (group[0] & group[1] & group[2]).pop()
        priority = ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27
        priorities.append(priority)
        group = []

print(sum(priorities))
