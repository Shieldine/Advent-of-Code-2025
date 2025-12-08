import math

import numpy as np

STOP = 1000

coords = []

with open("../input/day_8.txt") as f:
    for line in f.readlines():
        coords.append([int(c) for c in line.strip().split(",")])

distances = {}

for point in coords:
    for second in coords:
        if point == second:
            continue

        if (tuple(second), tuple(point)) in distances:
            continue

        distances[(tuple(point), tuple(second))] = np.linalg.norm(np.array(point) - np.array(second))

distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

circuits = [[tuple(coord)] for coord in coords]
lengths = []

idx = 0

last_connection = None

for k, v in distances.items():
    if idx == STOP:
        lengths = [len(circuit) for circuit in circuits]
    idx += 1

    first, second = k

    first_circuit = None
    second_circuit = None

    for circuit in circuits:
        if first in circuit:
            first_circuit = circuit
        if second in circuit:
            second_circuit = circuit

    if first_circuit == second_circuit:
        continue

    if first_circuit is not None and second_circuit is None:
        first_circuit.append(second)
    elif second_circuit is not None and first_circuit is None:
        second_circuit.append(first)
    elif first_circuit is not None and second_circuit is not None:
        first_circuit.extend(second_circuit)
        circuits.remove(second_circuit)

    if len(circuits) == 1:
        last_connection = first, second
        break

lengths.sort(reverse=True)

print(math.prod(lengths[:3]))
print(last_connection[0][0] * last_connection[1][0])
