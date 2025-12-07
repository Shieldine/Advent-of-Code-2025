beams = set()
diagram = []


def print_formatted(d):
    for r in d:
        print(" ".join(r))


with open("../input/day_7.txt") as f:
    for line in f:
        diagram.append(list(line.strip()))

for row in range(len(diagram)):
    for col in range(len(diagram[row])):
        if diagram[row][col] == "S":
            beams.add((row, col))

splitters = set()

while len(beams) > 0:
    new_beams = set()
    for beam in beams:
        if beam[0] + 1 > len(diagram) - 1:
            continue
        if diagram[beam[0] + 1][beam[1]] == ".":
            new_beams.add((beam[0] + 1, beam[1]))
            diagram[beam[0] + 1][beam[1]] = "|"
        elif diagram[beam[0] + 1][beam[1]] == "^":
            new_beams.add((beam[0], beam[1] - 1))
            new_beams.add((beam[0], beam[1] + 1))
            splitters.add((beam[0] + 1, beam[1]))

    beams = new_beams

print(len(splitters))
