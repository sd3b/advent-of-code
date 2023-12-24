import re
from itertools import product

# SLOOOW

total = 0

for line in open("input.txt"):
    spring, conditions = line.split()
    conditions = [int(x) for x in conditions.split(",")]
    wildcards = [idx for idx, char in enumerate(spring) if char == "?"]

    for wildcard_combination in product('.#', repeat = len(wildcards)):
        possible_spring = list(spring)

        for idx, bit in zip(wildcards, wildcard_combination):
            possible_spring[idx] = bit

        possible_spring = "".join(possible_spring)

        if [len(x) for x in re.findall("#+", possible_spring)] == conditions:
            total += 1

print("Part 1:", total)
