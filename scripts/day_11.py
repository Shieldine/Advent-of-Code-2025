devices = {}

paths = 0

with open("../input/day_11.txt") as f:
    for line in f.readlines():
        line = line.strip()

        fr, to = line.split(":")

        devices[fr.strip()] = [t.strip() for t in to.split(" ") if t != ""]


def traverse(current):
    cur = 0

    if current == "out":
        return 1

    for d in devices[current]:
        cur += traverse(d)

    return cur


print(traverse("you"))
