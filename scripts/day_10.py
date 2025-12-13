import re
from itertools import combinations

total = 0


def find_optimal_presses(options, goal):
    best = len(options)

    for k in range(len(options)):
        combs = combinations(options, k)

        for comb in combs:
            cur = [False for _ in range(len(goal))]

            for button in comb:
                for num in button:
                    cur[num] = not cur[num]

            if cur == goal:
                if k < best:
                    return k

    return best


with open("../input/day_10.txt") as f:
    for line in f.readlines():
        line = line.strip()

        states = re.findall(r"[.#]", line)
        buttons = re.findall(r"\([\d,]+\)", line)

        lights = [char == "#" for char in states]
        b = []

        for button in buttons:
            b.append([int(c) for c in button.replace("(", "").replace(")", "").split(",")])

        total += find_optimal_presses(b, lights)

print(total)
