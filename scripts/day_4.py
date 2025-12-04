accessible = 0

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

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == ".":
            continue
        count = 0
        for direction in DIRECTIONS:
            ni = i + direction[0]
            nj = j + direction[1]
            if 0 <= ni < len(m) and 0 <= nj < len(m[ni]):
                if m[i + direction[0]][j + direction[1]] != ".":
                    count += 1

        if count < 4:
            accessible += 1

print(accessible)
