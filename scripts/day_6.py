import math

nums = []
operands = []
raw = []

with open("../input/day_6.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        line += " "
        raw.append(list(line))

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

flipped = []

for i in range(len(raw[0])):
    flipped.append([])
    for j in range(len(raw)):
        flipped[i].append(raw[j][i])

nums = []
operand = ""

total = 0

for col in flipped:
    if all('' == s or s.isspace() for s in col):
        if operand == "*":
            total += math.prod(nums)
        elif operand == "+":
            total += sum(nums)
        nums = []
        operand = ""
        continue
    if "*" not in col and "+" not in col:
        nums.append(int(''.join(col)))
    else:
        nums.append(int(''.join(col[:-1])))
        operand = col[-1]

print(total)
