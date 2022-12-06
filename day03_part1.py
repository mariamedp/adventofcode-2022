# fname = 'inputs/day03.test.txt'
fname = 'inputs/day03.txt'

with open(fname, 'r') as f:
    rucksacks = [l.strip() for l in f.readlines()]

priorities = []
for content in rucksacks:
    half = len(content) // 2
    comp1, comp2 = content[:half], content[half:]
    item = (set(comp1) & set(comp2)).pop()
    priority = ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27
    priorities.append(priority)

print(sum(priorities))
