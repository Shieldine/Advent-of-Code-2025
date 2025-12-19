import re
from itertools import combinations

from z3 import Int, Optimize, Sum

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]

total = 0
total2 = 0


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


def find_minimum_button_presses(buttons, targets):
    variables = {}
    opt = Optimize()

    for i in range(len(buttons)):
        variables[alphabet[i]] = Int(alphabet[i])
        opt.add(variables[alphabet[i]] >= 0)

    equations = [[0 for _ in range(len(buttons))] for _ in range(len(targets))]
    for i in range(len(targets)):
        for j in range(len(buttons)):
            equations[i][j] = 1 if i in buttons[j] else 0

    for i in range(len(targets)):
        equation_sum = Sum([equations[i][j] * variables[alphabet[j]]
                            for j in range(len(buttons))])
        opt.add(equation_sum == targets[i])

    total_sum = Sum(list(variables.values()))
    opt.minimize(total_sum)

    if opt.check():
        model = opt.model()
        result = sum([model[variables[alphabet[i]]].as_long() for i in range(len(buttons))])
        return result
    return None


with open("../input/day_10.txt") as f:
    for line in f.readlines():
        line = line.strip()

        states = re.findall(r"[.#]", line)
        buttons = re.findall(r"\([\d,]+\)", line)
        levels = re.findall(r"\{[\d,]+}", line)[0].replace("{", "").replace("}", "")

        lights = [char == "#" for char in states]
        b = []
        a = [int(char) for char in levels.split(",")]

        for button in buttons:
            b.append([int(c) for c in button.replace("(", "").replace(")", "").split(",")])

        total += find_optimal_presses(b, lights)
        total2 += find_minimum_button_presses(b, a)

print(total)
print(total2)
