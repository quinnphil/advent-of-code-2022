def read_data(path_data):
    with open(path_data) as fh:
        data = fh.read()
        rows = [[int(j) for j in i.split('\n')] for i in data.split('\n\n')]
    return rows


data = read_data('data/day01_p1.txt')

print('Part 1')
max_cal = max([sum(c) for c in data])
print(max_cal)

print('\nPart 2')
top_3 = sum(sorted([sum(c) for c in data])[-3:])
print(top_3)
