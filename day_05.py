import re
from collections import defaultdict

def read_data(path_data):
    with open(path_data) as fh:
        data_state, data_commands = fh.read().split("\n\n")
        data_state = data_state.splitlines()
        data_commands = data_commands.splitlines()

    return data_state, data_commands

def get_state(data_state):
    state = defaultdict(list)

    for line in data_state:

        if '[' in line:
            for i in range(1, len(line) - 1, 4):
                if line[i].isalpha():
                    state[(i - 1) // 4].append(line[i])

    return state

def part1(state, commands):

    for line in commands:
        n, s_from, s_to = map(int, re.findall(r'\d+', line))
        state[s_to - 1] = state[s_from - 1][:n][::-1] + state[s_to - 1]
        state[s_from - 1] = state[s_from - 1][n:]
    return (''.join(state[i][0] for i in range(len(state))))


def part2(state, commands):
    for line in commands:
        n, s_from, s_to = map(int, re.findall(r'\d+', line))
        state[s_to - 1] = state[s_from - 1][:n] + state[s_to - 1]
        state[s_from - 1] = state[s_from - 1][n:]
    return (''.join(state[i][0] for i in range(len(state))))

data_state, data_commands = read_data('data/day05.txt')


print("Part 1")
state = get_state(data_state)
print(part1(state, data_commands))

print("Part 2")
state = get_state(data_state)
print(part2(state, data_commands))
