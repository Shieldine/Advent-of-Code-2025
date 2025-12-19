import itertools

import shapely
from shapely.prepared import prep

coords = []

with open("../input/day_9.txt") as f:
    for line in f:
        first, second = line.strip().split(",")
        coords.append((int(first), int(second)))

combs = itertools.combinations(coords, 2)
polygon = shapely.geometry.Polygon([(x, -y) for x, y in coords])
prepared_polygon = prep(polygon)

largest = 0
second_largest = 0

for comb in combs:
    area = (abs(comb[0][0] - comb[1][0]) + 1) * (abs(comb[0][1] - comb[1][1]) + 1)

    if area > largest:
        largest = area

    if area < second_largest:
        continue

    x1, y1 = comb[0]
    x2, y2 = comb[1]

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    rectangle = shapely.geometry.box(min_x, -max_y, max_x, -min_y)

    if prepared_polygon.covers(rectangle):
        second_largest = area

print(largest)
print(second_largest)
