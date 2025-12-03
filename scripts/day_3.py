import itertools

joltage = 0
joltage_2 = 0

with open("../input/day_3.txt") as f:
    banks = f.readlines()

banks = [bank.strip() for bank in banks]

for bank in banks:
    parts = [bank[i] for i in range(len(bank))]

    combs = itertools.combinations(parts, 2)
    combs = [''.join(com) for com in combs]

    joltage += max([int(com) for com in combs])

    num = ['0' for _ in range(12)]

    for i in range(12):
        highest = 0
        dex = 0
        for idx, part in enumerate(parts):
            if idx > len(parts) - (12-i):
                continue
            if highest < int(part):
                highest = int(part)
                dex = idx

        num[i] = str(highest)
        parts = parts[dex+1:]

    joltage_2 += int(''.join(num))

print(joltage)
print(joltage_2)
