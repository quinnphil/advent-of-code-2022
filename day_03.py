
def read_data(path_data):
    with open(path_data) as fh:
        lines = fh.read().splitlines()

    return lines

def part_1(rucksacks):
    common = []
    for line in rucksacks:

        mid = int(len(line) / 2)
        r1 = set(line[0: mid])
        r2 = set(line[mid:])

        common.extend(list(r1.intersection(r2)))
    return common


def part_2(rucksacks):
    common = []
    groups = []
    group = []
    for i, line in enumerate(rucksacks):
        line = line.strip()
        group.append(line)
        if (i+1) % 3 == 0:
            groups.append(group)
            group = []

    for group in groups:
        common.extend(set(list(group[0])).intersection(set(list(group[1]))).intersection(set(list(group[2]))))


    return common


def score(items):
    map_p = {chr(i + 96): i for i in range(1, 27)} | {chr(i + 64): i + 26 for i in range(1, 27)}

    return sum([map_p[i] for i in items])

print("P1 - Test")
rucksacks = read_data('data/day03_test.txt')
common = part_1(rucksacks)
print(score(common))

print("\nP1 - Actual")
rucksacks = read_data('data/day03_p1.txt')
common = part_1(rucksacks)
print(score(common))

print("\n\nP2 - Test")
rucksacks = read_data('data/day03_test.txt')
common = part_2(rucksacks)
print(score(common))


print("\n\nP2 - Actual")
rucksacks = read_data('data/day03_p1.txt')
common = part_2(rucksacks)
print(score(common))
