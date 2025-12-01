START = 50
MAX = 100

cur = START
count_1 = 0
count_2 = 0

with open("./input/day_1.txt") as f:
    for line in f:
        change = 0
        if "R" in line:
            change = int(line.replace("R","").strip())
        if "L" in line:
            change = -int(line.replace("L","").strip())

        rots = abs(change) // MAX
        count_2 += rots

        change += rots * 100 if change < 0 else -rots * 100

        if change < 0 < cur and cur + change <= 0:
            count_2 += 1
        elif change > 0 and cur + change > MAX-1:
            count_2 += 1

        cur = (cur + change) % MAX

        if cur == 0:
            count_1 += 1


print(count_1)
print(count_2)