# fname = 'inputs/day07.test.txt'
fname = 'inputs/day07.txt'

with open(fname, 'r') as f:
    terminal_output = [l.strip() for l in f.readlines()]


dirs = {
    '/': {'_path_': ['/'], '_total_size_': 0, '_parent_': None}
}
sizes = {}

current_dir = dirs['/']
for line in terminal_output:
    if line.startswith('$ cd '):
        dirname = line[5:]
        if dirname == '..':
            current_dir = current_dir['_parent_']
        elif dirname == '/':
            current_dir = dirs['/']
        else:
            current_dir = current_dir[dirname]
    elif line.startswith('dir'):
        dirname = line.split(' ')[1]
        current_dir[dirname] = {
            '_path_': current_dir['_path_'] + [dirname],
            '_total_size_': 0,
            '_parent_': current_dir
        }
    elif not line.startswith('$'):
        file_size, file_name = line.split()
        current_dir[file_name] = int(file_size)
        dir_toupdate = current_dir
        while dir_toupdate is not None:
            dir_toupdate['_total_size_'] += int(file_size)
            sizes['/'.join(dir_toupdate['_path_'])] = dir_toupdate['_total_size_']
            dir_toupdate = dir_toupdate['_parent_']

sum([ds for ds in sizes.values() if ds <= 100000])


### Part 2

DISK_SPACE = 70000000
NEEDED = 30000000

current_space = DISK_SPACE - sizes['/']
extra_needed = NEEDED - current_space

min([ds for ds in sizes.values() if ds >= extra_needed])
