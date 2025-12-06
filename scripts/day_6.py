import math

nums = []
operands = []

with open("../input/day_6.txt") as f:
    for line in f:
        if "+" in line or "*" in line:
            operands = list(line.strip().replace(" ", ""))
        else:
            cur = line.strip().split(" ")
            cur = [int(c) for c in cur if c != ""]
            nums.append(cur)

total = 0

for idx, op in enumerate(operands):
    if op == "+":
        total += sum([num[idx] for num in nums])
    else:
        total += math.prod([num[idx] for num in nums])

print(total)
