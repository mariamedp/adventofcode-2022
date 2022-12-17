# fname = 'inputs/day05.test.txt'
fname = 'inputs/day05.txt'

with open(fname, 'r') as f:
    text_input = f.read()

drawing, instructions = text_input.split('\n\n')
drawing = drawing.split('\n')[::-1]
instructions = instructions.strip().split('\n')

ncolumns = len(drawing[0]) // 3
columns = []
for i in range(ncolumns):
    column = []
    posc = 1 + 4 * i
    for layer in drawing[1:]:
        letter = layer[posc]
        if letter != ' ':
            column.append(letter)
    columns.append(column)


for instr in instructions:
    fields = instr.split(' ')
    nmove = int(fields[1])
    ind_from = int(fields[3]) - 1
    ind_to = int(fields[5]) - 1
    for i in range(nmove):
        letter = columns[ind_from].pop()
        columns[ind_to].append(letter)

print(''.join(col[-1] for col in columns))
