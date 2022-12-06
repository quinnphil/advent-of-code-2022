def read_data(path_data):
    with open(path_data) as fh:
        data = fh.read()
        data.strip()
    return data


def find_marker(data, marker_len):
    for i in range(0, len(data)-marker_len):
        slice = data[i:i+marker_len]
        if len(set(slice)) == marker_len:
            return i + marker_len


data = read_data('data/day06.txt')

print('Part 1')
print(find_marker(data, 4))

print('\nPart 2')
print(find_marker(data, 14))
