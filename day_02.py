def read_data(path_data):
    with open(path_data) as fh:
        data = fh.read()
        rows = [[j for j in i.split(' ')] for i in data.split('\n')]
        rows = rows[0:-1]
    return rows

map_hands = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}


def score_round(ply, opp):
    points = 0
    if opp == 3 and ply == 1:
        points = 6 + ply
    elif opp == 1 and ply == 3:
        points = ply
    elif ply > opp:
        points = 6 + ply
    # Draw
    elif ply == opp:
        points = 3 + ply
    # Loss
    else:
        points = 0 + ply
    return points

def play_part1(rounds):
    score = 0
    for r in rounds:
        opp = map_hands[r[0]]
        ply = map_hands[r[1]]

        score += score_round(ply, opp)

    return score


def play_part2(rounds):
    score = 0
    for r in rounds:
        ply = -1
        opp = map_hands[r[0]]
        res = r[1]

        # Draw
        if res == "Y":
            ply = opp
        # Lose
        elif res == "X":
            ply = opp - 1
            if ply == 0:
                ply = 3
        # Win
        elif res == "Z":
            ply = (opp % 3) + 1

        points = score_round(ply, opp)

        score += points

    return score



print("Part 1")
data = read_data('data/day02_p1.txt')
print(play_part1(data))

print("Part 2")
print(play_part2(data))

