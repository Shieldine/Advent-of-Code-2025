DIRECTIONS = [
    [1, 0],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
    [0, 1],
    [0, -1],
    [-1, 0]
]

with open("../input/day_4.txt") as f:
    m = f.readlines()

m = [list(l.strip()) for l in m]


def remove_rolls(roll_map):
    to_remove = []
    for i in range(len(roll_map)):
        for j in range(len(roll_map[i])):
            if roll_map[i][j] == ".":
                continue
            count = 0
            for direction in DIRECTIONS:
                ni = i + direction[0]
                nj = j + direction[1]
                if 0 <= ni < len(m) and 0 <= nj < len(m[ni]):
                    if roll_map[i + direction[0]][j + direction[1]] != ".":
                        count += 1

            if count < 4:
                to_remove.append((i, j))

    for pair in to_remove:
        roll_map[pair[0]][pair[1]] = "."

    return len(to_remove)


removed = remove_rolls(m)
total = removed
print(removed)

while removed > 0:
    removed = remove_rolls(m)
    total += removed

print(total)
