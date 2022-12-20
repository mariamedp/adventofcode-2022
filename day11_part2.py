# fname = 'inputs/day11.test.txt'
fname = 'inputs/day11.txt'

with open(fname, 'r') as f:
    text_input = f.read()


monkeys = []
for text_monkey in text_input.split('\n\n'):
    monkey_info = text_monkey.split('\n')
    monkeys.append({
        'items': [int(i) for i in monkey_info[1].replace('  Starting items: ', '').split(', ')],
        'op': monkey_info[2].replace('  Operation: new = ', ''),
        'test_div': int(monkey_info[3].replace('  Test: divisible by ', '')),
        'throw': {
            True: int(monkey_info[4].replace('    If true: throw to monkey ', '')),
            False: int(monkey_info[5].replace('    If false: throw to monkey ', '')),
        },
        'total_inspected': 0
    })

divisor = 1
for m in monkeys:
    divisor *= m['test_div']

for round in range(10000):
    for i in range(len(monkeys)):
        while len(monkeys[i]['items']) > 0:
            monkeys[i]['total_inspected'] += 1
            old = monkeys[i]['items'].pop(0)
            new = eval(monkeys[i]['op'])  # f(old)
            new = new % divisor  # Update worry level
            test_result = new % monkeys[i]['test_div'] == 0
            monkey_throw = monkeys[i]['throw'][test_result]
            monkeys[monkey_throw]['items'].append(new)


max_insp = sorted([m['total_inspected'] for m in monkeys], reverse=True)
max_insp[0] * max_insp[1]
