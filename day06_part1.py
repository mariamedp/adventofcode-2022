# fname = 'inputs/day06.test.txt'
fname = 'inputs/day06.txt'

with open(fname, 'r') as f:
    text_input = f.read()

NDIF = 4

recent_markers = list(text_input[:NDIF])
for i in range(NDIF, len(text_input)):
    if len(set(recent_markers)) == NDIF:
        print(i)
        break
    _ = recent_markers.pop(0)
    recent_markers.append(text_input[i])
