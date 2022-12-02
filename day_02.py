def read_data(path_data):
    with open(path_data) as fh:
        data = fh.read()
        rows = [[j for j in i.split(' ')] for i in data.split('\n')]
        rows = rows[0:-1]
    return rows


map_hands = {a: (1+((ord(a) + 5) % 10) % 3) for a in list("ABCXYZ")}


def score_round(ply, opp):
    points = 0
    if opp == 3 - ((4-ply) % 3): points = 6 + ply       # Win
    elif opp % 3 == (ply + 1) % 3: points = 0 + ply     # Lose
    else:
        points = 3 + ply                                # Draw

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
        match r[1]:
            case "Y": ply = opp                 # Draw
            case "X": ply = 3 - (4 - opp) % 3   # Lose
            case "Z": ply = (opp % 3) + 1       # Win
        score += score_round(ply, opp)
    return score


rounds = read_data('data/day02_p1.txt')

print("Part 1")
print(play_part1(rounds))

print("Part 2")
print(play_part2(rounds))

