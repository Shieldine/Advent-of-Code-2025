invalids_1 = 0
invalids_2 = 0

with open("../input/day_2.txt") as f:
    ranges = f.readlines()[0].strip().split(",")

single_cache = {}
multi_cache = {}


def check_repetitions(number: int) -> int:
    if number in multi_cache:
        return multi_cache[number]

    num_str = str(number)

    for l in range(1, len(num_str) + 1):
        sub_str = num_str[:l]

        if sub_str == num_str:
            multi_cache[number] = 0
            return 0

        repeated = True

        for part in range(0, len(num_str), l):
            if num_str[part:part + l] != sub_str:
                repeated = False
                break

        if repeated:
            multi_cache[number] = number
            return number

    multi_cache[number] = 0
    return 0


def check_single_repetition(number: int) -> int:
    if number in single_cache:
        return single_cache[number]

    first, second = str(i)[:int(len(str(i)) / 2)], str(i)[int(len(str(i)) / 2):]
    if first == second:
        single_cache[number] = number
        return number

    single_cache[number] = 0
    return 0


for entry in ranges:
    start, end = entry.split("-")
    if start[0] == "0":
        invalids_1 += int(start)

    if end[0] == "0":
        invalids_1 += int(end)

    for i in range(int(start), int(end) + 1):
        invalids_1 += check_single_repetition(i)
        invalids_2 += check_repetitions(i)

print(invalids_1)
print(invalids_2)
