def read_data(path_data):
    with open(path_data) as fh:
        lines = fh.read().splitlines()

    return lines

def get_sections(lines):
    sections = []
    for line in lines:

        sections.append([[int(h) for h in x.split('-')] for x in line.split(',')])


    return sections

def get_is_contained(section):
    is_contained = False
    s0 = section[0]
    s1 = section[1]

    if s0[0] >= s1[0] and s0[1] <= s1[1]:
        is_contained = True
    elif s1[0] >= s0[0] and s1[1] <= s0[1]:
        is_contained = True

    return is_contained

def get_is_any_overlap(section):
    is_overlap = False
    s0 = range(section[0][0], section[0][1] + 1)
    s1 = range(section[1][0], section[1][1] + 1)

    overlap = list(set(s0).intersection(set(s1)))
    is_overlap = len(overlap) > 0
    print(section)
    print(overlap)

    print("\n")

    return is_overlap


print("Part 1")
data = read_data('data/day04_p1.txt')
# data = read_data('data/day04_p1_test.txt')
sections = get_sections(data)
print(sections)
contained = []
for section in sections:
    contained.append(get_is_contained(section))
print(sum(contained))

data = read_data('data/day04_p1_test.txt')
print("\nPart 2")
contained = []
for section in sections:
    contained.append(get_is_any_overlap(section))
print(sum(contained))

# 729