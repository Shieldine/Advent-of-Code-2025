import copy

diagram = []

with open("../input/day_7.txt") as f:
    for line in f:
        diagram.append(list(line.strip()))

start = (0, diagram[0].index("S"))


def traverse(d, b):
    splitters = set()
    new_beams = set()

    for beam in b:
        if beam[0] + 1 > len(d) - 1:
            continue
        if d[beam[0] + 1][beam[1]] == ".":
            new_beams.add((beam[0] + 1, beam[1]))
            d[beam[0] + 1][beam[1]] = "|"
        elif d[beam[0] + 1][beam[1]] == "^":
            new_beams.add((beam[0], beam[1] - 1))
            new_beams.add((beam[0], beam[1] + 1))
            splitters.add((beam[0] + 1, beam[1]))

    if len(new_beams) == 0:
        return len(splitters)

    return len(splitters) + traverse(d, new_beams)


print(traverse(copy.deepcopy(diagram), {start}))

path_cache = {}


def traverse_single(d, beam):
    paths = 0

    if beam in path_cache:
        return path_cache[beam]

    if beam[0] + 1 > len(d) - 1:
        return 1
    if d[beam[0] + 1][beam[1]] == ".":
        result = traverse_single(d, (beam[0] + 1, beam[1]))
        path_cache[beam] = paths + result
        return paths + result
    elif d[beam[0] + 1][beam[1]] == "^":
        result = traverse_single(d, (beam[0], beam[1] - 1)) + traverse_single(d, (beam[0], beam[1] + 1))
        path_cache[beam] = paths + result
        return paths + result


print(traverse_single(diagram, start))
