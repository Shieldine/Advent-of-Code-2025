devices = {}

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


cache = {}


def find_paths(current, need_dac, need_fft):
    cache_key = (current, need_dac, need_fft)
    if cache_key in cache:
        return cache[cache_key]

    if current == "out":
        return 1 if (not need_dac and not need_fft) else 0

    still_need_dac = need_dac and (current != "dac")
    still_need_fft = need_fft and (current != "fft")

    num = 0
    for d in devices[current]:
        num += find_paths(d, still_need_dac, still_need_fft)

    cache[cache_key] = num
    return num


print(traverse("you"))

count = 0

for d in devices["svr"]:
    count += find_paths(d, True, True)

print(count)
