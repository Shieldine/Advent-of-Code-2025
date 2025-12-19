import itertools

import shapely
from shapely import Point

coords = []

with open("../input/day_9.txt") as f:
    for line in f:
        first, second = line.strip().split(",")
        coords.append((int(first), int(second)))

combs = itertools.combinations(coords, 2)
polygon = shapely.geometry.Polygon([(x, -y) for x, y in coords])

largest = 0
second_largest = 0

for comb in combs:
    area = (abs(comb[0][0] - comb[1][0]) + 1) * (abs(comb[0][1] - comb[1][1]) + 1)

    if area > largest:
        largest = area

    tiled = 0
    x1, y1 = comb[0]
    x2, y2 = comb[1]

    all_inside = True
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if polygon.covers(Point(x, -y)):
                tiled += 1
            else:
                all_inside = False
                break

    if not all_inside:
        continue

    if tiled > second_largest:
        second_largest = tiled

print(largest)
print(second_largest)
