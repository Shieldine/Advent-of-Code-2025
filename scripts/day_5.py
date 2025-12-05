ranges = []
ids = []

with open("../input/day_5.txt") as f:
    for line in f:
        if "-" in line:
            start, end = line.strip().split("-")
            ranges.append([int(start), int(end)])
        elif line == "\n":
            continue
        else:
            ids.append(int(line.strip()))

fresh = 0

for i in ids:
    for r in ranges:
        if r[0] <= i <= r[1]:
            fresh += 1
            break

range_counter = 0
joined_ranges = []

ranges.sort()

joined_ranges.append(ranges[0])

for i in range(1, len(ranges)):
    start, end = joined_ranges[-1]
    ns, ne = ranges[i]

    if ns <= end + 1:
        joined_ranges[-1][1] = max(end, ne)
    else:
        joined_ranges.append(ranges[i])

for r in joined_ranges:
    range_counter += r[1] - r[0] + 1

print(fresh)
print(range_counter)
