beams = set()
diagram = []


def print_formatted(d):
    for r in d:
        print(" ".join(r))


with open("../input/day_7.txt") as f:
    for line in f:
        diagram.append(list(line.strip()))

beams.add((0, diagram[0].index("S")))


def traverse(d, b):
    splitters = set()
    new_beams = set()

    for beam in b:
        if beam[0] + 1 > len(diagram) - 1:
            continue
        if diagram[beam[0] + 1][beam[1]] == ".":
            new_beams.add((beam[0] + 1, beam[1]))
            diagram[beam[0] + 1][beam[1]] = "|"
        elif diagram[beam[0] + 1][beam[1]] == "^":
            new_beams.add((beam[0], beam[1] - 1))
            new_beams.add((beam[0], beam[1] + 1))
            splitters.add((beam[0] + 1, beam[1]))

    if len(new_beams) == 0:
        return splitters

    return splitters | traverse(d, new_beams)


print(len(traverse(diagram, beams)))
