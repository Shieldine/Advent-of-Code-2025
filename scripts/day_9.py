import itertools

coords = []

with open("../input/day_9.txt") as f:
    for line in f:
        first, second = line.strip().split(",")
        coords.append((int(first), int(second)))

combs = itertools.combinations(coords, 2)

largest = 0

for comb in combs:
    area = (abs(comb[0][0] - comb[1][0]) + 1) * (abs(comb[0][1] - comb[1][1]) + 1)

    if area > largest:
        largest = area

print(largest)
